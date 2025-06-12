'''
    Author: Brayden Rhee
    Date: June 13, 2025
    Program Name: NASA APOD Auto Downloader & Wallpaper Setter
    https://github.com/midnflyr
'''
import requests
from datetime import datetime, timedelta, timezone

API_KEY = "YOUR_API_KEY"

today = datetime.now(timezone.utc).date()
yesterday = today - timedelta(days=1)

event_types = ["CME", "FLR", "SEP", "MPC", "RBE", "HSS", "WSAEnlilSimulations"]
display_names = {
    "CME": "CME",
    "FLR": "FLR",
    "SEP": "SEP",
    "MPC": "MPC",
    "RBE": "RBE",
    "HSS": "HSS",
    "WSAEnlilSimulations": "WSA_ES"
}
event_count_summary = {}

for event in event_types:
    url = f"https://api.nasa.gov/DONKI/{event}?startDate={yesterday}&endDate={today}&api_key={API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"[ERROR] Failed to fetch {event} data: {response.status_code}")
        event_count_summary[event] = -1
        continue

    data = response.json()
    count = len(data)
    event_count_summary[event] = count

    if count > 0:
        print(f"\n== ALERT: {count} {event} EVENTS DETECTED ==")
        for item in data:
            time = item.get("startTime") or item.get("time21_5") or item.get("eventTime") or "N/A"
            link = item.get("link", "N/A")
            print(f"[{event}] Time: {time}")
            if link != "N/A":
                print(f"Details: {link}")
            print("-" * 60)
    else:
        print(f"== ALERT: NO {event} EVENTS DETECTED ==")

summary_parts = [
    f"{count} {display_names[etype]}" for etype, count in event_count_summary.items() if count >= 0
]
summary_string = ", ".join(summary_parts)
print(f"\n======\nSUMMARY\n\n{summary_string}\n\nDetected in the past 24 hours.\n======\n")
