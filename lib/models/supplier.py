from models.__init__ import CURSOR, CONN

class Supplier:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location
    
    @property
    def name(self):
        return self._name 
    @name.setter
    def name(self, name):
        if isinstance(name, str) and (1 <= len(name) <= 15):
            self._name = name
        else:
            raise ValueError("Name must be string and be between 1 - 15 characters long")
    
    @property
    def location(self):
        return self._location
    @location.setter
    def location(self, location):
        if isinstance(location, str) and (1 <= len(location) <= 20):
            self._location = location
        else:
            raise ValueError("Location needs to be a string and between 1 - 20 characters long")
        
    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS suppliers (
            id INTEGER PRIMARY KEY,
            name TEXT,
            location TEXT
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS suppliers;
        """
        CURSOR.execute(sql)
        CONN.commit()