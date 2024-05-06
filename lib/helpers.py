# lib/helpers.py
from models.supplier import Supplier
from models.item import Items


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
        print(f"Supplier {id_} has been deleted")
    else:
        print(f"Could not delete supplier {id_}")

#Items helper function

def list_all_items():
    pass

def find_item_by_id():
    pass

def create_item():
    pass

def update_item():
    pass

def delete_item():
    pass