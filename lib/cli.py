# lib/cli.py

from helpers import (
    exit_program,
    list_all_suppliers,
    find_supplier_by_name,
    find_supplier_by_id,
    create_supplier,
    update_supplier,
    delete_supplier
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
            find_supplier_by_name()
        elif choice == "3":
            find_supplier_by_id()
        elif choice == "4":
            create_supplier()
        elif choice == "5":
            update_supplier()
        elif choice == "6":
            delete_supplier()
        else:
            print("Invalid choice")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. See all Suppliers and Locations")
    print("2. Find Supplier by name")
    print("3. Find Supplier by ID")
    print("4. Create a Supplier")
    print("5. Update a Supplier")
    print("6. Delete a Supplier")


if __name__ == "__main__":
    main()
