import csv

FILE_NAME = "contacts.csv"

def load_contacts():

    contacts = []
    try:
        with open(FILE_NAME, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                contacts.append(row)
    except FileNotFoundError:
        print("No contacts file found. Starting with an empty contact list.")
    return contacts
