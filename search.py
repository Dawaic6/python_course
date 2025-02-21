# Function to filter events by category
def filter_by_category(events: List[Dict], category: str) -> List[Dict]:
    return [event for event in events if event["category"] == category]

# Function to search events by keyword in title or description
def search_events(events: List[Dict], keyword: str) -> List[Dict]:
    keyword = keyword.lower()
    return [event for event in events if keyword in event["title"].lower() or keyword in event["description"].lower()]

# Function to filter events based on date
def filter_by_date(events: List[Dict], future=True) -> List[Dict]:
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    if future:
        return [event for event in events if event["date"] >= today]
    else:
        return [event for event in events if event["date"] < today]
    