import json

def add_entry(entries):
    amount = float(input("Enter amount: "))
    description = input("Enter description: ")
    entry = {"amount": amount, "description": description}

    entries.append(entry)

def view_entries(entries):
    for entry in entries:
        print(f"{entry['description']}: '$'{entry['amount']}")

def main():
    try:
        with open("budget.json", "r") as file:
            entries = json.load(file)
    except FileNotFoundError:
        entries = []

    while True:
        print("1. Add entry")
        print("2. View entries")
        print("3. Exit")
        choice = input("Enter choice (1/2/3): ")
        if choice == '1':
            add_entry(entries)
        elif choice == '2':
            view_entries(entries)
        elif choice == '3':
            with open("budget.json", "w") as file:
                json.dump(entries, file)
            break
        else:
            print("Invalid choice")
if __name__=="__main__":
    main()