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

    @property
    def serial_number(self):
        return self._serial_number
    @serial_number.setter
    def serial_number(self, serial_number):
        if isinstance(serial_number, int) and (serial_number >= 6):
            self._serial_number = serial_number
        else:
            raise ValueError("Serial number must be type integer and must be atleast 6 characters long")
    
    @property
    def supplier_id(self):
        return self._supplier_id
    @supplier_id.setter
    def supplier_id(self, supplier_id):
        if isinstance(supplier_id, int) and Supplier.find_by_id(supplier_id):
            self._supplier_id = supplier_id
        else:
            raise ValueError("Supplier id must refrence supplier database")