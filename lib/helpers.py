# lib/helpers.py
from models.supplier import Supplier
from models.item import Item


def exit_program():
    print("Goodbye!")
    exit()

def page_2():
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("Enter search to see specific supplier items")
    print("Enter add if you wish to add a new supplier")
    print("Enter update if you wish to delete a supplier")
    print("Enter delete if you wish to update a supplier")
    print("Enter back if you wish to main menu again")
    print("------------------------------------------------")
    print("------------------------------------------------")

def page_3():
    print("------------------------------------------------")
    print("------------------------------------------------")
    print("Enter add to create new item")
    print("Enter update to update an item")
    print("Enter delete to delete an item")
    print("Enter back to see previous page")
    print("------------------------------------------------")
    print("------------------------------------------------")

#Supplier helper functions

def list_all_suppliers():
    suppliers = Supplier.get_all()
    for supplier in suppliers:
        print(supplier)

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
    id_ = input("Enter suppliers number: ")
    items = Item.find_by_supplier_id(id_)
    if items:
        for item in items:
            print(item)
    else:
        print("Couldn't find supplier")

#Items helper function

def list_all_items():
    items = Item.get_all()
    for item in items:
        print(item)

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
    id_ = input("Enter item number you wish to update: ")
    if item := Item.find_by_id(id_):
        try:
            name = input("Enter updated item name: ")
            item.name = name
            serial_number = int(input("Enter updated item serial number: "))
            item.serial_number = serial_number
            supplier_id = int(input("Enter updated item supplier number: "))
            item.supplier_id = supplier_id

            item.update()
            print(f"UPDATED: {item}")
        except Exception as exc:
            print("Could not update item", exc)
    else:
        print(f"Could not find item number: {id_}")

def delete_item():
    id_ = input("Enter item you wish to delete: ")
    if item := Item.find_by_id(id_):
        item.delete()
        print(f"DELETED: {item}")
    else:
        print(f"Item number {id_} not found.")