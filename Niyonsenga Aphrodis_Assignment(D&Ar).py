#Q77. Event Registration Platform: Stack for undoing registrations, queue for processing event 
# registrations, and list to manage event details.

from collections import deque

# events list
events = [{"id": 1, "name": "Music Festivol", "date": "2024-10-20", "location": "Huye", "description": "A conference about the latest in Music."},
{"id": 2, "name": "Art Exhibition", "date": "2024-11-15", "location": "Rubavu", "description": "Showcasing modern art."},
{"id": 3, "name": "Matches", "date": "2024-11-18", "location": "Kigali Pele stadium", "description": "APR fc Vs Rion sport."},
{"id": 4, "name": "best project", "date": "2024-11-25", "location": "Kigali", "description": "Showing best project of year."}
]
   
registration_queue = deque()
undo_stack = []

def display_events():
    print("\nUpcoming Events:")
    for event in events:
        print(f"{event['id']}: {event['name']} | Date: {event['date']} | Location: {event['location']}")
        print(f"  Description: {event['description']}")
    print()

def register_event(event_id, name, email, payment):
    event = next((event for event in events if event["id"] == event_id), None)
    if event:
        registration = {"event": event, "name": name, "email": email, "payment": payment}
        registration_queue.append(registration)
        undo_stack.append({"action": "register", **registration})
        print(f"Successfully registered {name} for {event['name']}!")
    else:
        print("Event not found!")

def undo_registration():
    if undo_stack:
        last_action = undo_stack.pop()
        if last_action["action"] == "register":
            # Create a registration dictionary for removal
            registration_to_remove = {"event": last_action["event"], "name": last_action["name"], "email": last_action["email"], "payment":last_action ["payment"]}
            # Check if it exists in the queue
            if registration_to_remove in registration_queue:
                registration_queue.remove(registration_to_remove)
                print(f"Registration for {last_action['name']} for {last_action['event']['name']} has been undone.")
            
   else:
        print("No actions to undo.")

def view_registrations():
    print("\nYour Registrations:")
    if registration_queue:
        for registration in registration_queue:
            event = registration["event"]
            print(f"Name: {registration['name']} - {event['name']} -{event['date']} - {event['location']} | Email: {registration['email']}")
    else:
        print("You have no registrations.")

def main():
    while True:
        display_events()
        print("1. Register for an event")
        print("2. View my registrations")
        print("3. Undo last registration")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            event_id = int(input("Enter event ID to register: "))
            name = input("Enter your name: ")
            email = input("Enter your email: ")
            payment = int(input(" Enter payment for event you chose   "))
            register_event(event_id, name, email,payment)
        elif choice == '2':
            view_registrations()
        elif choice == '3':
            undo_registration()
        elif choice == '4':
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
