def search_contacts(contacts):

    print("\nSearch by:")
    print("1. Name")
    print("2. Phone")
    print("3. Email")
    print("4. Address")

    field_choice = input("Choose a field to search by (1-4): ")
    if field_choice == "1":
        field = "Name"
    elif field_choice == "2":
        field = "Phone"
    elif field_choice == "3":
        field = "Email"
    elif field_choice == "4":
        field = "Address"
    else:
        print("Invalid choice! Returning to menu.")
        return

    query = input(f"Enter {field}: ").lower()

    results = [
        contact for contact in contacts
        if query in contact[field].lower()
    ]

    if not results:
        print("No matching contacts found.")
    else:
        print(f"{'Name':<20} {'Phone':<15} {'Email':<30} {'Address':<30}")
        print("-" * 95)
        for contact in results:
            print(f"{contact['Name']:<20} {contact['Phone']:<15} {contact['Email']:<30} {contact['Address']:<30}")
