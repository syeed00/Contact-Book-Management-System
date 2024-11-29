def add_contact(contacts):

    name = input("Enter Name: ")
    if not name.isalpha():
        print("Error: Name must only contain alphabets!")
        return contacts

    phone = input("Enter Phone Number: ")
    if not phone.isdigit():
        print("Error: Phone number must be numeric!")
        return contacts

    # Ensure unique phone number
    if any(contact["Phone"] == phone for contact in contacts):
        print("Error: Phone number already exists!")
        return contacts

    email = input("Enter Email (optional): ")
    address = input("Enter Address: ")

    new_contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
    contacts.append(new_contact)
    print("Contact added successfully!")
    return contacts