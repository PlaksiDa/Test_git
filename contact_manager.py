import os
from file_manager import save_contacts

class ContactManager:
    def __init__(self):
        self.contacts = {}

    def show_all_contacts(self):
        if not self.contacts:
            print("Телефонный справочник пуст.")
        else:
            print("Все контакты:")
            for name, number in self.contacts.items():
                print(f"Имя: {name}, Телефон: {number}")

    def add_contact(self):
        name = input("Введите имя контакта: ")
        number = input("Введите номер телефона контакта: ")
        self.contacts[name] = number
        print("Контакт добавлен.")

    def find_contact(self):
        name = input("Введите имя контакта для поиска: ")
        if name in self.contacts:
            print(f"Имя: {name}, Телефон: {self.contacts[name]}")
        else:
            print("Контакт не найден.")

    def edit_contact(self):
        name = input("Введите имя контакта для редактирования: ")
        if name in self.contacts:
            new_number = input("Введите новый номер телефона: ")
            self.contacts[name] = new_number
            print("Контакт изменен.")
        else:
            print("Контакт не найден.")

    def delete_contact(self):
        name = input("Введите имя контакта для удаления: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Контакт удален.")
        else:
            print("Контакт не найден.")

    def save_contacts(self):
        save_contacts(self.contacts)