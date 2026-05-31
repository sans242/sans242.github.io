"""
Garmin Connect -> Supabase Sync Script
Runs via GitHub Actions to pull all running activities and store in Supabase.
"""

import os
import json
import sys
import io
from datetime import datetime, timedelta

# Fix encoding for Windows
if sys.platform == 'win32':
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
    sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

from garminconnect import Garmin
from supabase import create_client, Client


# --- Config ---
GARMIN_EMAIL = os.environ.get("GARMIN_EMAIL")
GARMIN_PASSWORD = os.environ.get("GARMIN_PASSWORD")
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")

BATCH_SIZE = 100  # Garmin API page size
ACTIVITY_TYPES = {"running", "trail_running", "treadmill_running", "track_running"}


def login_garmin():
    """Authenticate with Garmin Connect."""
    print("[LOGIN] Logging into Garmin Connect...")
    client = Garmin(GARMIN_EMAIL, GARMIN_PASSWORD)
    client.login()
    print("[LOGIN] Login successful")
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


def main():
    # Validate env vars
    missing = []
    for var in ["GARMIN_EMAIL", "GARMIN_PASSWORD", "SUPABASE_URL", "SUPABASE_KEY"]:
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


if __name__ == "__main__":
    main()
