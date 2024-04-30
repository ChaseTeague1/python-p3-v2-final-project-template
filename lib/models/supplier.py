from models.__init__ import CURSOR, CONN

class Supplier:
    all = {}

    def __init__(self, name, location, id=None):
        self.id = id
        self.name = name
        self.location = location

    def __repr__(self):
        return f"<Supplier {self.id}: {self.name}, {self.location}>"
    
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
    
    def save(self):
        sql = """
            INSERT INTO suppliers (name, location)
            VALUES (?, ?)
        """
        CURSOR.execute(sql, (self.name, self.location))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def instance_from_db(cls, row):
        supplier = cls.all.get(row[0])
        if supplier:
            supplier.name = row[1]
            supplier.location = row[2]
        else:
            supplier = cls(row[1], row[2])
            supplier.id = row[0]
            cls.all[supplier.id] = supplier
        return supplier
    
    @classmethod
    def create(cls, name, location):
        supplier = cls(name, location)
        supplier.save()
        return supplier
    
    def delete(self):
        sql = """
            DELETE FROM suppliers
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        del type(self).all[self.id]
        self.id = None

    def update(self):
        sql = """
            UPDATE suppliers 
            SET name = ?, location = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.name, self.location, self.id))
        CONN.commit()

    @classmethod
    def find_by_id(cls, id):
        sql = """
            SELECT * FROM suppliers
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None
    
    @classmethod
    def get_all(cls):
        sql = """
            SELECT *
            FROM suppliers
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows ]
        