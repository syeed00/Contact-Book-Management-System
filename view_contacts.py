def view_contacts(contacts):

    if not contacts:
        print("No contacts found.")
        return

    print(f"{'Name':<20} {'Phone':<15} {'Email':<30} {'Address':<30}")
    print("-" * 95)
    for contact in contacts:
        print(f"{contact['Name']:<20} {contact['Phone']:<15} {contact['Email']:<30} {contact['Address']:<30}")
