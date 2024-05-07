# lib/cli.py

from helpers import (
    exit_program,
    list_all_suppliers,
    find_supplier_by_id,
    create_supplier,
    update_supplier,
    delete_supplier,
    create_item
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_suppliers()
        elif choice == "2":
            find_supplier_by_id()
        elif choice == "3":
            create_supplier()
        elif choice == "4":
            update_supplier()
        elif choice == "5":
            delete_supplier()
        elif choice == "6":
            create_item()
        else:
            print("Invalid choice")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all Suppliers and Locations")
    print("2. Find Supplier by ID")
    print("3. Create a Supplier")
    print("4. Update a Supplier")
    print("5. Delete a Supplier")
    print("6: Create an Item")


if __name__ == "__main__":
    main()
