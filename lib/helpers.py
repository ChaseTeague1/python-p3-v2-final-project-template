# lib/helpers.py
from models.supplier import Supplier
from models.item import Item
from colorama import Fore


def exit_program():
    print("Goodbye!")
    exit()

def page_2():
    print(Fore.MAGENTA + "------------------------------------------------" + Fore.RESET)
    print("------------------------------------------------")
    print("1. Enter search to see specific supplier items")
    print("2. Enter add if you wish to add a new supplier")
    print("3. Enter update if you wish to delete a supplier")
    print("4. Enter delete if you wish to update a supplier")
    print("5. Enter items to see all items")
    print("6. Enter back if you wish to main menu again")
    print("------------------------------------------------")
    print(Fore.RED + "------------------------------------------------" + Fore.RESET)

def page_3():
    print(Fore.MAGENTA + "------------------------------------------------" + Fore.RESET)
    print("------------------------------------------------")
    print("1. Enter add to create new item")
    print("2. Enter update to update an item")
    print("3. Enter delete to delete an item")
    print("4. Enter back to see previous page")
    print("------------------------------------------------")
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
    id_ = input("Enter supplier number you wish to update: ")
    if supplier := Supplier.find_by_id(id_):
        try: 
            name = input("Enter udpated name: ")
            supplier.name = name
            location = input("Enter updated location: ")
            supplier.location = location
            supplier.update()
            print(f"UPDATED: {supplier}")
        except Exception as exc:
            print("Could not update supplier", exc)

def delete_supplier():
    id_ = input("Enter suppliers number: ")
    if supplier := Supplier.find_by_id(id_):
        supplier.delete()
        print(f"DELETED: {supplier}")
    else:
        print(f"Could not delete supplier {id_}")

def list_supplier_items():
    suppliers = Supplier.get_all()
    for i, supplier in enumerate(suppliers, start =1):
        print(f"{i}: {supplier}")
        items = Item.find_by_supplier_id(supplier.id)
        if items:
            for j, item in enumerate(items, start=1):
                print(f" {i}: {j}: {item}")
        else:
            print("No items found for this supplier")

#Items helper function

def list_all_items():
    item_print()

def create_item():
    name = input("Enter item name: ")
    serial_number = int(input("Enter item serial number: "))
    supplier_id = input("Enter supplier number for item: ")
    try: 
        item = Item.create(name, serial_number, supplier_id)
        print(f"CREATED: {item}")
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
            print(f"UPDATED: {item}")
        except Exception as exc:
            print("Could not update item", exc)
    else:
        print(f"Could not find item number: {name}")

def delete_item():
    name = input("Enter name of item you wish to delete: ")
    if item := Item.find_by_name(name):
        item.delete()
        print(f"DELETED: {item}")
    else:
        print(f"Item number {name} not found.")