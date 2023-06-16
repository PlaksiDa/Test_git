class Menu:
    def __init__(self, contact_manager):
        self.contact_manager = contact_manager

    def print_menu(self):
        print("Меню:")
        print("1. Показать все контакты")
        print("2. Добавить контакт")
        print("3. Найти контакт")
        print("4. Изменить контакт")
        print("5. Удалить контакт")
        print("6. Выйти")

    def handle_choice(self, choice):
        if choice == "1":
            self.contact_manager.show_all_contacts()
        elif choice == "2":
            self.contact_manager.add_contact()
        elif choice == "3":
            self.contact_manager.find_contact()
        elif choice == "4":
            self.contact_manager.edit_contact()
        elif choice == "5":
            self.contact_manager.delete_contact()
        elif choice == "6":
            self.contact_manager.save_contacts()
            exit()
        else:
            print("Некорректный выбор.")