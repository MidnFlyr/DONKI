# NASA DONKI Console Alert System

This Python project fetches space weather event data from NASA's DONKI (Space Weather Database Of Notifications, Knowledge, Information) API and displays real-time alerts in the console based on events that occurred in the past 24 hours.

A simple automation project using real-time space data and structured scripting.

## Features

- Retrieves recent space weather events such as CME, FLR, SEP, HSS, etc.
- Filters only events from the past 24 hours
- Displays each event's timestamp and detail link (if available)
- Prints a clean summary of total events detected per type

## Requirements

- Python
- requests library

Install dependencies:

'''
pip install requests
'''

## API Key Setup

1. Get your NASA API key from https://api.nasa.gov
2. Replace the value of `API_KEY` in `main.py` with your actual API key:

'''
API_KEY = "your_actual_api_key_here"
'''

Note: Do not share your API key.

## How to Run

'''
python main.py
'''

The script will:

- Connect to the DONKI API
- Fetch all supported space weather event types
- Display alerts for events detected in the past 24 hours
- Print a summary report at the end

## Example Output

'''
== ALERT: 10 CME EVENTS DETECTED ==
[CME] Time: 2025-06-11T15:36Z
Details: https://...
------------------------------------------------------------
== ALERT: NO FLR EVENTS DETECTED ==

======
SUMMARY

10 CME, 0 FLR, 0 SEP, 0 MPC, 0 RBE, 0 HSS, 12 WSA_ES

Detected in the past 24 hours.
======
'''

Thank you.