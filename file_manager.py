import os

def open_contacts():
    try:
        filename = os.path.join('Sem_10', 'contacts.txt')
        with open(filename, 'r') as file:
            contacts = {}
            for line in file:
                name, number = line.strip().split(',')
                contacts[name] = number
            return contacts
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    filename = os.path.join('Sem_10', 'contacts.txt')
    with open(filename, 'w') as file:
        for name, number in contacts.items():
            file.write(f"{name},{number}\n")