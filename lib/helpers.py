# lib/helpers.py
from models.supplier import Supplier
from models.item import Item


def exit_program():
    print("Goodbye!")
    exit()

#Supplier helper functions

def list_all_suppliers():
    suppliers = Supplier.get_all()
    for supplier in suppliers:
        print(supplier)

def find_supplier_by_id():
    id_ = input("Enter supplier id: ")
    supplier = Supplier.find_by_id(id_)
    print((supplier) if supplier else print(f"Supplier not found"))

def create_supplier():
    name = input("Enter new supplier name: ")
    location = input("Enter new location: ")
    try:
        supplier = Supplier.create(name, location)
        print(f"CREATED: {supplier}")
    except Exception as exc:
        print("Error cannont create new supplier", exc)

def update_supplier():
    id_ = input("Enter supplier id you wish to update: ")
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
    id_ = input("Enter suppliers id: ")
    if supplier := Supplier.find_by_id(id_):
        supplier.delete()
        print(f"DELETED: {supplier}")
    else:
        print(f"Could not delete supplier {id_}")

#Items helper function

def list_all_items():
    items = Item.get_all()
    for item in items:
        print(item)

def find_item_by_id():
    id_ = input("Enter item id: ")
    item = Item.find_by_id(id_)
    print((item) if item else print(f"Could not find item {id_}"))

def create_item():
    name = input("Enter item name: ")
    serial_number = int(input("Enter item serial number: "))
    supplier_id = input("Enter supplier id for item: ")
    try: 
        item = Item.create(name, serial_number, supplier_id)
        print(f"CREATED: {item}")
    except Exception as exc:
        print("Failed to create item", exc)

def update_item():
    id_ = input("Enter item id you wish to update: ")
    if item := Item.find_by_id(id_):
        try:
            name = input("Enter updated item name: ")
            item.name = name
            serial_number = int(input("Enter updated item serial number: "))
            item.serial_number = serial_number
            supplier_id = int(input("Enter updated item supplier id: "))
            item.supplier_id = supplier_id

            item.update()
            print(f"UPDATED: {item}")
        except Exception as exc:
            print("Could not update item", exc)
    else:
        print(f"Could not find item id: {id_}")

def delete_item():
    id_ = input("Enter item you wish to delete: ")
    if item := Item.find_by_id(id_):
        item.delete()
        print(f"DELETED: {item}")
    else:
        print(f"Item id {id_} not found.")