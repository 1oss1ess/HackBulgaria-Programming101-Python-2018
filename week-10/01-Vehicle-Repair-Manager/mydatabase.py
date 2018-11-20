import sqlite3


class MyDB:
    def __init__(self):
        self.conn = sqlite3.connect('vehicle_management.db')
        self.c = self.conn.cursor()

    def query(self, query, params=None):
        if params is None:
            self.c.execute(query)
        else:
            for param in params:
                self.c.execute(query, param)
        self.conn.commit()

    def __del__(self):
        self.conn.close()
