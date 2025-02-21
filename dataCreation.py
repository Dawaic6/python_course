import datetime
import json
import csv
from typing import List, Dict

# Sample event data
events = [
    {"title": "Tech Conference", "date": "2025-08-10", "category": "Tech", "location": " San Francisco ", "description": "Annual technology conference."},
    {"title": "Food Truck Rally", "date": "2025-07-20", "category": "Food", "location": "Los Angeles", "description": "Try delicious food from food trucks!"},
    {"title": "Music Fest", "date": "2025-06-15", "category": "Music", "location": "New York", "description": "A festival featuring live bands."},
    {"title": "Art Expo", "date": "2024-05-05", "category": "Arts", "location": "Chicago", "description": "Showcasing modern and classical art."},
    {"title": "Basketball Finals", "date": "2025-09-30", "category": "Sports", "location": "Miami", "description": "The championship game of the season."}
]
print(events)