import csv

FILE_NAME = "contacts.csv"

def save_contacts(contacts):

    with open(FILE_NAME, "w", newline="") as file:
        fieldnames = ["Name", "Phone", "Email", "Address"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
    print("Contacts saved successfully.")
