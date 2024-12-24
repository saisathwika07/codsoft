# Contact Book Program

def display_menu():
    print("\n--- Contact Book Menu ---")
    print("1. View Contacts")
    print("2. Add Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Exit")

def view_contacts(contacts):
    if not contacts:
        print("\nNo contacts found!")
    else:
        print("\nContacts:")
        for name, number in contacts.items():
            print(f"{name}: {number}")

def add_contact(contacts):
    name = input("\nEnter the contact name: ").strip()
    if name in contacts:
        print("This contact already exists!")
    else:
        number = input("Enter the phone number: ").strip()
        contacts[name] = number
        print(f"Contact '{name}' added successfully!")

def update_contact(contacts):
    name = input("\nEnter the contact name to update: ").strip()
    if name in contacts:
        number = input("Enter the new phone number: ").strip()
        contacts[name] = number
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found!")

def delete_contact(contacts):
    name = input("\nEnter the contact name to delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found!")

def main():
    contacts = {}
    while True:
        display_menu()
        choice = input("\nEnter your choice: ").strip()
        if choice == "1":
            view_contacts(contacts)
        elif choice == "2":
            add_contact(contacts)
        elif choice == "3":
            update_contact(contacts)
        elif choice == "4":
            delete_contact(contacts)
        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

if _name_ == "_main_":
    main()