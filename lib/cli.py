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
    page_2,
    page_3,
    list_supplier_items
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
                if choice == "back":
                    menu()
                    break
                elif choice == "add":
                    create_supplier()
                elif choice == "delete":
                    delete_supplier()
                elif choice == "update":
                    update_supplier()
                elif choice == "search":
                    id = input("Enter suppliers number: ")
                    list_supplier_items(id)
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
                            break
                        else:
                            print("Invalid choice!")
                        list_supplier_items(id)
                else: 
                    print("Invalid choice!")
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
    import pyfiglet
    from colorama import Fore
    print(Fore.BLUE + pyfiglet.figlet_format("WELCOME", font="big") + Fore.RESET)
    print(Fore.WHITE + pyfiglet.figlet_format("                    TO", font="big"))
    print(Fore.CYAN + pyfiglet.figlet_format("       INVENTORY \n           MANAGER", font="small") + Fore.RESET)
    print("              Please Press 1 To See Your Suppliers")
    print("")



if __name__ == "__main__":
    main()
