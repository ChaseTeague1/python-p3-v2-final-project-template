# lib/helpers.py
from models.supplier import Supplier


def exit_program():
    print("Goodbye!")
    exit()

def list_all_suppliers():
    suppliers = Supplier.get_all()
    for supplier in suppliers:
        print(supplier)

def find_supplier_by_name():
    pass

def find_supplier_by_id():
    id_ = input("Enter supplier id: ")
    supplier = Supplier.find_by_id(id_)
    print((supplier) if supplier else print(f"Supplier not found"))

def create_supplier():
    pass

def update_supplier():
    pass

def delete_supplier():
    pass