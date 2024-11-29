def remove_contact(contacts):

    phone = input("Enter the phone number of the contact to remove: ")
    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            print("Contact removed successfully!")
            return contacts
    print("Error: No contact found with that phone number.")
    return contacts
