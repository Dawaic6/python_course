from collections import defaultdict

# Function to count events by category
def count_events_by_category(events: List[Dict]) -> Dict[str, int]:
    category_count = defaultdict(int)
    for event in events:
        category_count[event["category"]] += 1
    return dict(category_count)

# Function to find events happening this week
def events_this_week(events: List[Dict]) -> List[Dict]:
    today = datetime.date.today()
    week_later = today + datetime.timedelta(days=7)
    return [event for event in events if today.strftime("%Y-%m-%d") <= event["date"] <= week_later.strftime("%Y-%m-%d")]

# Function to generate a location summary
def location_summary(events: List[Dict]) -> Dict[str, List[str]]:
    location_data = defaultdict(list)
    for event in events:
        location_data[event["location"]].append(event["title"])
    return dict(location_data)
