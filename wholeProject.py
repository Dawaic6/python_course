# Function to load events from a CSV file
def load_events_from_csv(filename: str) -> List[Dict]:
    events = []
    with open(filename, "r", newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            events.append(row)
    return events

# Function to save events to a JSON file
def save_events_to_json(events: List[Dict], filename: str):
    with open(filename, "w") as file:
        json.dump(events, file, indent=4)

# Command-line interaction
def main():
    filename = "events.csv"
    events = load_events_from_csv(filename)
    events = clean_events(events)

    while True:
        print("\n1. Search events")
        print("2. Filter by category")
        print("3. View category statistics")
        print("4. Save to JSON")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            keyword = input("Enter a keyword: ")
            results = search_events(events, keyword)
            print(results)

        elif choice == "2":
            category = input("Enter category: ")
            results = filter_by_category(events, category)
            print(results)

        elif choice == "3":
            print(count_events_by_category(events))

        elif choice == "4":
            save_events_to_json(events, "events.json")
            print("Data saved to events.json")

        elif choice == "5":
            break

if __name__ == "__main__":
    main()
# Compare this snippet from wholeProject.py:
# from dataCreation import events   
# from dataReporting import count_events_by_category, events_this_week, location_summary
# from dataValidation import clean_events
# from search import filter_by_category, search_events