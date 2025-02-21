# Function to validate date format
def is_valid_date(date_str: str) -> bool:
    try:
        datetime.datetime.strptime(date_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Function to validate category
def is_valid_category(category: str) -> bool:
    valid_categories = {"Music", "Food", "Tech", "Arts", "Sports"}
    return category in valid_categories

# Function to clean event data
def clean_events(events: List[Dict]) -> List[Dict]:
    today = datetime.datetime.today().strftime("%Y-%m-%d")
    cleaned_events = []

    for event in events:
        if is_valid_date(event["date"]) and event["date"] >= today:
            event["title"] = event["title"].title()
            event["location"] = event["location"].strip()  # Remove extra spaces
            if is_valid_category(event["category"]):
                cleaned_events.append(event)

    return cleaned_events

# Clean the event data
events = clean_events(events)
print(events)