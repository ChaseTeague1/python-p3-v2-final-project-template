# lib/cli.py

from helpers import (
    exit_program,
    list_all_suppliers,
    create_supplier,
    update_supplier,
    delete_supplier,
    create_item,
    list_all_items,
    delete_item,
    update_item,
    page_2
)


def main():
    menu()
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_suppliers()
            while True:
                page_2()
                choice = input("> ")
                if choice == "add":
                    create_supplier()
                list_all_suppliers()

                if choice == "delete":
                    delete_supplier()
                list_all_suppliers()

        elif choice == "3":
            create_supplier()
        elif choice == "4":
            update_supplier()
        elif choice == "5":
            delete_supplier()
        elif choice == "6":
            list_all_items()
        elif choice == "7":
            create_item()
        elif choice == "9":
            update_item()
        elif choice == "10":
            delete_item()
        else:
            print("Invalid choice")



def menu():
    print("****** Welcome to Inventory Manager ******\n----- A place where you can see and manage all your items and where they come from! -----")
    print("To see all current suppliers press 1")


if __name__ == "__main__":
    main()
