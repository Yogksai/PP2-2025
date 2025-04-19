from csv import DictReader
from create import insert
from update import update_by_id
from delete import delete_user_by_value
from read import get_people


if __name__ == '__main__':
    while True:
        print("""
        1. Add user
        2. Update user
        3. Delete user
        4. Search user
        5. Add User from CSV
        0. Exit
        """)
        choice = input("Choose action: ")

        if choice == "1":
            name = input("Enter name: ")
            second_name = input("Enter second name: ")
            last_name = input("Enter last name: ")
            phone_number = input("Enter phone: ")

            insert(name, second_name, last_name, phone_number)

        elif choice == "2":
            person_id = int(input("Enter person_id: "))
            name = input("Enter new name (or leave empty): ") or None
            phone = input("Enter new phone (or leave empty): ") or None
            update_by_id(person_id, new_name=name, new_phone=phone)

        elif choice == "3":
            value = input("Enter name or phone to delete: ")
            delete_user_by_value(value)

        elif choice == "4":
            value = input("Enter name or phone to search: ")
            get_people(value)
        elif choice == "5":
            with open("contacts.csv", mode="r", newline="") as data:
                contacts = DictReader(data)
                for contact in contacts:
                    insert(contact["name"], contact["second_name"], contact["last_name"], contact["phone"])

        elif choice == "0":
            break

        else:
            print("Invalid choice. Try again.")   