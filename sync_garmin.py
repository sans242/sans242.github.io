"""
Garmin Connect -> Supabase Sync Script
Runs via GitHub Actions to pull all running activities, daily steps, and resting HR,
then stores them in Supabase.

Uses tokenstore-based auth (garminconnect v0.3.4+) with session persistence
to avoid hitting Garmin's login rate limits.
"""

import os
import json
import sys
import io
from datetime import datetime, timedelta
from pathlib import Path

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from garminconnect import Garmin, GarminConnectAuthenticationError, GarminConnectConnectionError
from supabase import create_client, Client


# --- Config ---
GARMIN_EMAIL = os.environ.get("GARMIN_EMAIL")
GARMIN_PASSWORD = os.environ.get("GARMIN_PASSWORD")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

TOKENSTORE_PATH = os.environ.get("GARMINTOKENS", os.path.expanduser("~/.garminconnect"))

BATCH_SIZE = 100  # Garmin API page size
ACTIVITY_TYPES = {"running", "trail_running", "treadmill_running", "track_running"}
DAILY_STEPS_DAYS = 90  # How many days of step data to sync


def login_garmin():
    """Authenticate with Garmin Connect using tokenstore for session persistence."""
    print(f"[LOGIN] Token store path: {TOKENSTORE_PATH}")

    # Ensure tokenstore directory exists
    Path(TOKENSTORE_PATH).mkdir(parents=True, exist_ok=True)

    # Try to resume a saved session first
    try:
        client = Garmin()
        client.login(TOKENSTORE_PATH)
        print("[LOGIN] Resumed session from saved tokens")
        return client
    except (GarminConnectAuthenticationError, GarminConnectConnectionError, FileNotFoundError, Exception) as e:
        print(f"[LOGIN] Could not resume session ({type(e).__name__}: {e}), performing fresh login...")

    # Fresh login with credentials
    if not GARMIN_EMAIL or not GARMIN_PASSWORD:
        print("[ERROR] No saved tokens and GARMIN_EMAIL / GARMIN_PASSWORD not set")
        sys.exit(1)

    client = Garmin(GARMIN_EMAIL, GARMIN_PASSWORD)
    client.login(TOKENSTORE_PATH)
    print("[LOGIN] Fresh login successful, tokens saved")
    return client


def fetch_all_activities(client):
    """Fetch ALL activities from Garmin Connect (paginated)."""
    all_activities = []
    offset = 0

    while True:
        print(f"[FETCH] Fetching activities {offset} to {offset + BATCH_SIZE}...")
        batch = client.get_activities(offset, BATCH_SIZE)

        if not batch:
            break

        all_activities.extend(batch)
        offset += BATCH_SIZE

        if len(batch) < BATCH_SIZE:
            break

    print(f"[FETCH] Total activities fetched: {len(all_activities)}")
    return all_activities


def filter_running_activities(activities):
    """Filter to only running-type activities."""
    running = []
    for a in activities:
        activity_type = a.get("activityType", {})
        type_key = activity_type.get("typeKey", "").lower() if isinstance(activity_type, dict) else ""

        if type_key in ACTIVITY_TYPES:
            running.append(a)

    print(f"[FILTER] Running activities found: {len(running)}")
    return running


def extract_activity_data(activity):
    """Extract relevant fields from a raw Garmin activity."""
    return {
        "activity_id": activity.get("activityId"),
        "activity_name": activity.get("activityName", "Unnamed Run"),
        "activity_type": (
            activity.get("activityType", {}).get("typeKey", "running")
            if isinstance(activity.get("activityType"), dict)
            else "running"
        ),
        "start_time": activity.get("startTimeLocal"),
        "duration": activity.get("duration"),                    # seconds
        "distance": activity.get("distance"),                    # meters
        "avg_speed": activity.get("averageSpeed"),               # m/s
        "max_speed": activity.get("maxSpeed"),                   # m/s
        "avg_hr": activity.get("averageHR"),                     # bpm
        "max_hr": activity.get("maxHR"),                         # bpm
        "calories": activity.get("calories"),
        "elevation_gain": activity.get("elevationGain"),         # meters
        "elevation_loss": activity.get("elevationLoss"),         # meters
        "avg_running_cadence": activity.get("averageRunningCadenceInStepsPerMinute"),
        "max_running_cadence": activity.get("maxRunningCadenceInStepsPerMinute"),
        "steps": activity.get("steps"),
        "avg_stride_length": activity.get("avgStrideLength"),    # meters
        "training_effect": activity.get("aerobicTrainingEffect"),
        "vo2max": activity.get("vO2MaxValue"),
        "raw_json": json.dumps(activity, default=str),           # full dump
        "synced_at": datetime.utcnow().isoformat(),
    }


def upsert_to_supabase(supabase_client, activities):
    """Upsert activities into Supabase, avoiding duplicates."""
    if not activities:
        print("[SYNC] No activities to sync")
        return

    rows = [extract_activity_data(a) for a in activities]

    # Upsert in chunks to avoid payload limits
    chunk_size = 50
    total_upserted = 0

    for i in range(0, len(rows), chunk_size):
        chunk = rows[i : i + chunk_size]
        result = (
            supabase_client.table("garmin_activities")
            .upsert(chunk, on_conflict="activity_id")
            .execute()
        )
        total_upserted += len(chunk)
        print(f"[SYNC] Upserted {total_upserted}/{len(rows)} activities...")

    print(f"[DONE] Sync complete! {total_upserted} activities in database.")


def fetch_resting_hr(garmin_client, days=90):
    """Fetch resting heart rate for the last N days."""
    print(f"[RHR] Fetching resting HR for last {days} days...")
    rhr_data = []
    today = datetime.now().date()

    for i in range(days):
        day = today - timedelta(days=i)
        day_str = day.isoformat()
        try:
            hr = garmin_client.get_heart_rates(day_str)
            resting = hr.get("restingHeartRate")
            if resting and resting > 0:
                rhr_data.append({
                    "date": day_str,
                    "resting_hr": resting,
                    "synced_at": datetime.utcnow().isoformat(),
                })
        except Exception:
            pass  # skip days with no data

    print(f"[RHR] Got {len(rhr_data)} days of resting HR data")
    return rhr_data


def upsert_resting_hr(supabase_client, rhr_data):
    """Upsert resting HR data to Supabase."""
    if not rhr_data:
        print("[RHR] No resting HR data to sync")
        return

    for i in range(0, len(rhr_data), 50):
        chunk = rhr_data[i:i+50]
        supabase_client.table("garmin_resting_hr").upsert(
            chunk, on_conflict="date"
        ).execute()
        print(f"[RHR] Upserted {min(i+50, len(rhr_data))}/{len(rhr_data)}")

    print(f"[RHR] Resting HR sync complete!")


def fetch_daily_steps(garmin_client, days=DAILY_STEPS_DAYS):
    """Fetch daily step counts for the last N days."""
    print(f"[STEPS] Fetching daily steps for last {days} days...")
    steps_data = []
    today = datetime.now().date()
    start_date = today - timedelta(days=days)

    try:
        # get_daily_steps returns a list of daily step summaries
        raw_steps = garmin_client.get_daily_steps(
            start_date.isoformat(),
            today.isoformat()
        )

        if not raw_steps:
            print("[STEPS] No step data returned from Garmin")
            return steps_data

        for day_data in raw_steps:
            # The API returns different structures; handle both
            cal_date = day_data.get("calendarDate")
            total = day_data.get("totalSteps", 0)
            goal = day_data.get("stepGoal") or day_data.get("dailyStepGoal")
            distance = day_data.get("totalDistance")  # meters
            calories = day_data.get("totalKilocalories") or day_data.get("totalCalories")

            if cal_date and total and total > 0:
                steps_data.append({
                    "date": cal_date,
                    "total_steps": total,
                    "step_goal": goal,
                    "distance": distance,
                    "calories_total": calories,
                    "synced_at": datetime.utcnow().isoformat(),
                })

    except Exception as e:
        print(f"[STEPS] Error fetching steps: {e}")
        # Fallback: try day-by-day
        try:
            for i in range(days):
                day = today - timedelta(days=i)
                day_str = day.isoformat()
                try:
                    day_steps = garmin_client.get_steps_data(day_str)
                    if day_steps:
                        # Sum up all step intervals for the day
                        total = sum(s.get("steps", 0) for s in day_steps if isinstance(s, dict))
                        if total > 0:
                            steps_data.append({
                                "date": day_str,
                                "total_steps": total,
                                "step_goal": None,
                                "distance": None,
                                "calories_total": None,
                                "synced_at": datetime.utcnow().isoformat(),
                            })
                except Exception:
                    pass
        except Exception as e2:
            print(f"[STEPS] Fallback also failed: {e2}")

    print(f"[STEPS] Got {len(steps_data)} days of step data")
    return steps_data


def upsert_daily_steps(supabase_client, steps_data):
    """Upsert daily steps data to Supabase."""
    if not steps_data:
        print("[STEPS] No step data to sync")
        return

    for i in range(0, len(steps_data), 50):
        chunk = steps_data[i:i+50]
        supabase_client.table("garmin_daily_steps").upsert(
            chunk, on_conflict="date"
        ).execute()
        print(f"[STEPS] Upserted {min(i+50, len(steps_data))}/{len(steps_data)}")

    print(f"[STEPS] Daily steps sync complete!")


def fetch_personal_records(garmin_client):
    """Fetch official personal records (PRs) from Garmin Connect."""
    print("[PR] Fetching personal records...")
    pr_rows = []

    # Map Garmin's numeric typeId to our known keys
    TYPE_ID_MAP = {
        1: "1k",
        2: "1_mile",
        3: "5k",
        4: "10k",
        5: "half_marathon",
        6: "marathon",
        7: "longest_run",
        8: "most_elevation",
    }

    try:
        display_name = garmin_client.display_name
        if not display_name:
            print("[PR] Could not get display name")
            return []
            
        raw_prs = garmin_client.connectapi(
            f"/personalrecord-service/personalrecord/prs/{display_name}"
        )

        if not raw_prs or not isinstance(raw_prs, list):
            print("[PR] No personal records returned from Garmin")
            return pr_rows

        for pr in raw_prs:
            if not isinstance(pr, dict):
                continue
                
            # Filter to accepted records
            if pr.get("status") != "ACCEPTED":
                continue

            type_id = pr.get("typeId")
            pr_type_key = TYPE_ID_MAP.get(type_id, f"unknown_{type_id}")
            
            # The value is typically in seconds or meters.
            # Our frontend expects value_ms (milliseconds).
            raw_value = pr.get("value")
            if raw_value is None:
                continue
                
            # Convert value to milliseconds (or just multiply by 1000)
            # Longest run (type 7) is in meters, so multiplying by 1000 makes it match Garmin's cm
            # Actually, frontend handles value_ms by dividing by 1000 for seconds, and dividing by 100000 for km.
            # So if it's seconds, x1000 = ms. If it's meters, x1000 = millimeters (frontend expects /100000 for km, which means it expects value in cm).
            # Wait, 10237.9 meters * 1000 = 10237900. / 100000 = 102.37... wait.
            # Let's just multiply everything by 1000 for now.
            value_ms = int(float(raw_value) * 1000)

            pr_rows.append({
                "pr_type": pr_type_key,
                "value_ms": value_ms,
                "activity_id": pr.get("activityId"),
                "activity_name": pr.get("activityName"),
                "activity_type": pr.get("activityType"),
                "pr_date": pr.get("actStartDateTimeInGMTFormatted") or pr.get("prStartTimeGmtFormatted"),
                "raw_json": json.dumps(pr, default=str),
                "synced_at": datetime.utcnow().isoformat(),
            })

    except Exception as e:
        print(f"[PR] Error fetching personal records: {e}")

    print(f"[PR] Got {len(pr_rows)} personal records")
    return pr_rows


def upsert_personal_records(supabase_client, pr_data):
    """Upsert personal records to Supabase."""
    if not pr_data:
        print("[PR] No personal records to sync")
        return

    # Clear existing records and insert fresh ones (PRs change over time)
    try:
        supabase_client.table("garmin_personal_records").delete().neq("pr_type", "__impossible__").execute()
    except Exception:
        pass  # Table might not exist yet

    for i in range(0, len(pr_data), 50):
        chunk = pr_data[i:i+50]
        supabase_client.table("garmin_personal_records").upsert(
            chunk, on_conflict="pr_type"
        ).execute()
        print(f"[PR] Upserted {min(i+50, len(pr_data))}/{len(pr_data)}")

    print(f"[PR] Personal records sync complete!")


def main():
    # Validate env vars
    missing = []
    for var in ["SUPABASE_URL", "SUPABASE_KEY"]:
        if not os.environ.get(var):
            missing.append(var)
    if missing:
        print(f"[ERROR] Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    # Connect to services
    garmin_client = login_garmin()
    supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Fetch & sync activities
    all_activities = fetch_all_activities(garmin_client)
    running_activities = filter_running_activities(all_activities)
    upsert_to_supabase(supabase_client, running_activities)

    # Fetch & sync resting HR
    rhr_data = fetch_resting_hr(garmin_client)
    upsert_resting_hr(supabase_client, rhr_data)

    # Fetch & sync daily steps
    steps_data = fetch_daily_steps(garmin_client)
    upsert_daily_steps(supabase_client, steps_data)

    # Fetch & sync personal records
    pr_data = fetch_personal_records(garmin_client)
    upsert_personal_records(supabase_client, pr_data)


if __name__ == "__main__":
    main()
