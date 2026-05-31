# -*- coding: utf-8 -*-
"""Create garmin_resting_hr table and sync resting HR data."""
import os, sys, io, json
from datetime import datetime, timedelta
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8', errors='replace')

os.environ["GARMIN_EMAIL"] = "sanskarshah242@gmail.com"
os.environ["GARMIN_PASSWORD"] = "Stanley%242"
os.environ["SUPABASE_URL"] = "https://uuzrzcnvieygjlihgwnb.supabase.co"
os.environ["SUPABASE_KEY"] = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6InV1enJ6Y252aWV5Z2psaWhnd25iIiwicm9sZSI6ImFub24iLCJpYXQiOjE3Nzc4MDE3OTEsImV4cCI6MjA5MzM3Nzc5MX0._LP_f3WtKPVEvVCG1Uqh5S5ARHSHF7maopdWIbWg7Mw"

from garminconnect import Garmin
from supabase import create_client

print("[1] Logging into Garmin...")
g = Garmin(os.environ["GARMIN_EMAIL"], os.environ["GARMIN_PASSWORD"])
g.login()
print("[1] OK")

print("[2] Fetching resting HR for last 90 days...")
rhr_data = []
today = datetime.now().date()
for i in range(90):
    day = today - timedelta(days=i)
    day_str = day.isoformat()
    try:
        hr = g.get_heart_rates(day_str)
        resting = hr.get("restingHeartRate")
        if resting and resting > 0:
            rhr_data.append({
                "date": day_str,
                "resting_hr": resting,
                "synced_at": datetime.utcnow().isoformat(),
            })
            if len(rhr_data) % 10 == 0:
                print(f"  {len(rhr_data)} days collected...")
    except Exception as e:
        pass

print(f"[2] Got {len(rhr_data)} days")
if rhr_data:
    print(f"  Latest: {rhr_data[0]['date']} = {rhr_data[0]['resting_hr']} bpm")
    print(f"  Oldest: {rhr_data[-1]['date']} = {rhr_data[-1]['resting_hr']} bpm")

print("[3] Upserting to Supabase...")
sb = create_client(os.environ["SUPABASE_URL"], os.environ["SUPABASE_KEY"])
for i in range(0, len(rhr_data), 50):
    chunk = rhr_data[i:i+50]
    try:
        sb.table("garmin_resting_hr").upsert(chunk, on_conflict="date").execute()
        print(f"  {min(i+50, len(rhr_data))}/{len(rhr_data)} done")
    except Exception as e:
        print(f"  ERROR: {e}")
        break

print("[DONE]")
