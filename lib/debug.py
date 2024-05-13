#!/usr/bin/env python3
# lib/debug.py

from models.supplier import Supplier
from models.item import Item


def database():
    Supplier.drop_table()
    Item.drop_table()
    Supplier.create_table()
    Item.create_table()

    toogle = Supplier.create("Toogle", "Texas, United States")
    megasoft = Supplier.create("Megasoft", "California, United States")
    bopple = Supplier.create("Bopple", "Albany, United States")
    
    Item.create("Laptop", 123456, toogle.id)
    Item.create("EyePhone", 654321, bopple.id)
    Item.create("Shutters", 87654321, megasoft.id)

    
database()