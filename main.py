import file_manager
import menu
from contact_manager import ContactManager

def main():
    contact_manager = ContactManager()
    menu_obj = menu.Menu(contact_manager)

    contact_manager.contacts = file_manager.open_contacts()

    while True:
        menu_obj.print_menu()
        choice = input("Введите номер операции: ")
        menu_obj.handle_choice(choice)

if __name__ == "__main__":
    main()