#!/usr/bin/env python3
# lib/debug.py

from models.__init__ import CONN, CURSOR
from models.supplier import Supplier



def database():
    Supplier.drop_table()
    Supplier.create_table()

    Supplier.create("Toogle", "Texas, United States")
    Supplier.create("Megasoft", "California, United States")
    
database()