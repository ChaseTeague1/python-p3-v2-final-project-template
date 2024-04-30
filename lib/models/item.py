from models.__init__ import CURSOR, CONN
from supplier import Supplier

class Item:
    all = {}

    def __init__(self, name, serial_number, supplier_id, id=None):
        self.id = id
        self.name = name
        self.serial_number = serial_number
        self.supplier_id = supplier_id

    def __repr__(self):
        return (
            f"<Item {self.id}: {self.name}, {self.job_title}, " +
            f"Supplier ID: {self.supplier_id}>" )
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a string and greater than 0")
