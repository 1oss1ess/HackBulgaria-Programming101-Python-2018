# import sqlite3


class BaseUser:
    def __init__(self, id, username, phone_number, email, address):
        self.id = id
        self.username = username
        self.phone_number = phone_number
        self.email = email
        self.address = address

    def get_username(self):
        return self.username

    def get_id(self):
        return self.id

    # @classmethod
    # def getAll(self):
    #     conn = sqlite3.connect('userdb.db')
    #     conn.row_factory = self.dict_factory
    #     c = conn.cursor()
    #     query = '''SELECT id, first_name, last_name FROM user'''
    #     c.execute(query)
    #     users = c.fetchall()
    #     result = []
    #     for item in users:
    #         client = Client(item['id'], item['first_name'], item['last_name'])
    #         result.append(client)
    #     conn.close()
    #     return result

    # def dict_factory(cursor, row):
    #     d = {}
    #     for idx, col in enumerate(cursor.description):
    #         d[col[0]] = row[idx]
    #     return d
