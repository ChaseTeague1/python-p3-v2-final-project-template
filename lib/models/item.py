from models.__init__ import CURSOR, CONN
from models.supplier import Supplier

class Item:
    all = {}

    def __init__(self, name, serial_number, supplier_id):
        self.name = name
        self.serial_number = serial_number
        self.supplier_id = supplier_id