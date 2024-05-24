# lib/helpers.py
from models.supplier import Supplier
from models.item import Item
from colorama import Fore


def exit_program():
    print("Goodbye!")
    exit()

def page_2():
    print(Fore.MAGENTA + "------------------------------------------------" + Fore.RESET)
    print(" ")
    print("1. Enter search to see specific supplier items")
    print("2. Enter add if you wish to add a new supplier")
    print("3. Enter update if you wish to delete a supplier")
    print("4. Enter delete if you wish to update a supplier")
    print("5. Enter items to see all items")
    print("6. Enter back if you wish to main menu again")
    print(" ")
    print(Fore.RED + "------------------------------------------------" + Fore.RESET)

def page_3():
    print(Fore.MAGENTA + "------------------------------------------------" + Fore.RESET)
    print(" ")
    print("1. Enter add to create new item")
    print("2. Enter update to update an item")
    print("3. Enter delete to delete an item")
    print("4. Enter back to see previous page")
    print(" ")
    print(Fore.RED + "------------------------------------------------" + Fore.RESET)

#Supplier helper functions



    #output messages using enumerate
    #for i, value in enumerate(values, start=1):
        #print(i, value)
    
def supplier_print():
    suppliers = Supplier.get_all()
    for i, supplier in enumerate(suppliers, start=1):
        print(f"{i}: {supplier.name}, {supplier.location}")

def item_print():
    items = Item.get_all()
    for i, item in enumerate(items, start=1):
        print(f"{i}: {item.name}, Serial Number: {item.serial_number}")


def list_all_suppliers():
    supplier_print()

def create_supplier():
    name = input("Enter new supplier name: ")
    location = input("Enter new location: ")
    try:
        supplier = Supplier.create(name, location)
        print(f"CREATED: {supplier}")
    except Exception as exc:
        print("Error cannont create new supplier", exc)

def update_supplier():
    index = int(input("Enter supplier number you wish to update: "))
    suppliers = Supplier.get_all()
    if 1 <= index <= len(suppliers):
        selected_supplier = suppliers[index - 1]
        try:
            name = input("Enter udpated name: ")
            selected_supplier.name = name
            location = input("Enter updated location: ")
            selected_supplier.location = location
            selected_supplier.update()
            print(f"UPDATED: {selected_supplier.name}")
        except Exception as exc:
            print("Could not update supplier", exc)

def delete_supplier():
    suppliers = Supplier.get_all()
    try:
        index = int(input("Enter number of supplier you wish to delete: "))
        if 1 <= index <= len(suppliers):
            selected_supplier = suppliers[index - 1]
            suppliers = Supplier.find_by_id(selected_supplier.id)
            if suppliers:
                selected_supplier.delete()
            else:
                print("unable to delete supplier, try again!")
        else:
            print("Invalid index!")
    except Exception as exc:
        raise ValueError("Supplier not found!", exc)


def list_supplier_items(selected_index):
    suppliers = Supplier.get_all()
    if 1 <= selected_index <= len(suppliers):
        selected_supplier = suppliers[selected_index - 1]
        items = Item.find_by_supplier_id(selected_supplier.id)
        if items:
            print(f"Items for {selected_supplier.name}:")
            for i, item in enumerate(items, start=1):
                print(f"{i}: {item.name}, Serial Number: {item.serial_number}")
        else:
            print(f"No items found for supplier {selected_supplier.name}.")
    else:
        print("Invalid supplier index.")

#Items helper function

def list_all_items():
    item_print()

def create_item():
    name = input("Enter item name: ")
    serial_number = int(input("Enter item serial number: "))
    supplier_id = input("Enter supplier number for item: ")
    try: 
        item = Item.create(name, serial_number, supplier_id)
        print(f"CREATED: {item.name}")
    except Exception as exc:
        print("Failed to create item", exc)

def update_item():
    index = int(input("Enter item number you wish to update: "))
    items = Item.get_all()
    if 1 <= index <= len(items):
        item = items[index - 1]
        try:
            name = input("Enter updated item name: ")
            item.name = name
            serial_number = int(input("Enter updated item serial number: "))
            item.serial_number = serial_number

            item.update()
            print(f"UPDATED: {item.name}")
        except Exception as exc:
            print("Could not update item", exc)
    else:
        print(f"Could not find item number: {name}")

def delete_item():
    items = Item.get_all()
    try: 
        index = int(input("Enter number of item you wish to delete: "))
        if 1 <= index <= len(items):
            selected_item = items[index - 1]
            items = Item.find_by_id(selected_item.id)
            if items:
                selected_item.delete()
            else:
                print("Not able to delete item, Try again!")
        else:
            print("Invalid index!")
    except Exception as exc:
        raise ValueError("Could not find item!", exc)