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
    page_2,
    page_3,
    list_supplier_items,
)

def handle_main_menu():
    menu()
    while True:
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            handle_suppliers_menu()
        else:
            print("Invalid choice!")

def handle_suppliers_menu():
    list_all_suppliers()
    while True:
        page_2()
        choice = input("> ")
        if choice == "back":
            handle_main_menu()
        elif choice == "add":
            create_supplier()
        elif choice == "delete":
            delete_supplier()
        elif choice == "update":
            update_supplier()
        elif choice == "items":
            list_all_items()
        elif choice == "search":
            selected_index = int(input("Enter supplier index: "))
            handle_items_menu(selected_index)
        else:
            print("Invalid choice!")
        list_all_suppliers()

def handle_items_menu(selected_index):
    list_supplier_items(selected_index)
    while True:
        page_3()
        choice = input("> ")
        if choice == "add":
            create_item()
        elif choice == "delete":
            delete_item()
        elif choice == "update":
            update_item()
        elif choice == "back":
            return
        else:
            print("Invalid choice!")
        list_supplier_items(selected_index)

def menu():
    import pyfiglet
    from colorama import Fore
    print(Fore.BLUE + pyfiglet.figlet_format("WELCOME", font="big") + Fore.RESET)
    print(Fore.WHITE + pyfiglet.figlet_format("                    TO", font="big"))
    print(Fore.CYAN + pyfiglet.figlet_format("       INVENTORY \n           MANAGER", font="small") + Fore.RESET)
    print(Fore.GREEN + "            Please Press 1 To See Your Suppliers" + Fore.RESET)
    print(Fore.RED + "               Please Press 0 To Exit Program" + Fore.RESET)
    print("")

if __name__ == "__main__":
    handle_main_menu()