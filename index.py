from add_contact import add_contact
from view_contacts import view_contacts
from remove_contact import remove_contact
from search_contacts import search_contacts
from save_contacts import save_contacts
from load_contacts import load_contacts

contacts = load_contacts()

while True:
    print("\nContact Book Management System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Remove Contact")
    print("5. Save and Exit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        contacts = add_contact(contacts)
    elif choice == "2":
        view_contacts(contacts)
    elif choice == "3":
        search_contacts(contacts)
    elif choice == "4":
        contacts = remove_contact(contacts)
    elif choice == "5":
        save_contacts(contacts)
        print("Contacts saved. Exiting... Goodbye!")
        break
    else:
        print("Invalid option! Please choose again.")
