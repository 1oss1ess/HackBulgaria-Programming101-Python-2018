import datetime
import sys
import re
from mydatabase import MyDB
from baseuser import BaseUser
from client import Client
from mechanic import Mechanic
from settings import *


db = MyDB()


def check_email(email):
    if re.match(EMAIL_REGEX, email):
        return False
    else:
        return True


def register():
    create_new = input('>>> yes or no ?\n')
    if create_new.lower() in ['y', 'yes']:
        user_type = input('Are you a Client or Mechanic?\n>>> ')
        if len(user_type) == 0:
            print('Invalid user type!')
            sys.exit()
        if user_type == 'Client':
            return register_client()
        elif user_type == 'Mechanic':
            return register_mechanic()
    else:
        return 'Your choice is no!'


def register_client():
    username = input('Provide user_name:\n>>> ')
    if len(username) == 0:
        print('Invalid user name!')
        sys.exit()
    phone_number = input("Provide phone_number:\n>>>")
    if len(phone_number) == 0:
        print('Invalid phone number!')
        sys.exit()
    email = input("Provide email:\n>>>")
    if len(email) == 0:
        print('Invalid email!')
        sys.exit()
    if check_email(email):
        print('wrong email address')
        sys.exit()
    address = input("Provide address:\n>>>")
    if len(address) == 0:
        print('Invalid address!')
        sys.exit()

    insert_sql = "INSERT INTO BaseUser (user_name, phone_number, email, address) VALUES (?, ?, ?, ?)"
    db.query(insert_sql, [(username, phone_number, email, address)])

    select_query = "SELECT id FROM BaseUser WHERE user_name = ? LIMIT 1"
    db.query(select_query, [(username,)])
    user_id = db.c.fetchone()

    insert_sql = "INSERT INTO Client (base_id) VALUES (?)"
    db.query(insert_sql, [user_id])

    return 'Thank you, {}\nWelcome to Vehicle Services!\nNext time you try to login, provide your user_name!'.format(username)


def register_mechanic():
    username = input('Provide user_name:\n>>> ')
    if len(username) == 0:
        print('Invalid user name!')
        sys.exit()
    phone_number = input("Provide phone_number:\n>>>")
    if len(phone_number) == 0:
        print('Invalid phone number!')
        sys.exit()
    email = input("Provide email:\n>>>")
    if len(email) == 0:
        print('Invalid email!')
        sys.exit()
    if check_email(email):
        print('wrong email address')
        sys.exit()
    address = input("Provide address:\n>>>")
    if len(address) == 0:
        print('Invalid address!')
        sys.exit()
    title = input("Provide title:\n>>>")
    if len(title) == 0:
        print('Invalid title!')
        sys.exit()
    service_name = input("Provide service_name:\n>>>")
    if len(service_name) == 0:
        print('Invalid service_name!')
        sys.exit()

    insert_sql = "INSERT INTO Service (name) VALUES (?)"
    db.query(insert_sql, [(service_name,)])

    insert_sql = "INSERT INTO BaseUser (user_name, phone_number, email, address) VALUES (?, ?, ?, ?)"
    db.query(insert_sql, [(username, phone_number, email, address)])

    select_query = "SELECT id FROM BaseUser WHERE user_name = ? LIMIT 1"
    db.query(select_query, [(username,)])
    user_id = db.c.fetchone()

    insert_sql = "INSERT INTO Mechanic (base_id, title) VALUES (?, ?)"
    db.query(insert_sql, [(user_id[0], title)])

    select_query = "SELECT id FROM Service WHERE name = ? LIMIT 1"
    db.query(select_query, [(service_name,)])
    service_id = db.c.fetchone()

    insert_sql = "INSERT INTO Mechanic_services (mechanic_id, service_id) VALUES (?, ?)"
    db.query(insert_sql, [(user_id[0], service_id[0])])

    return 'Thank you, {}\nWelcome to Vehicle Services!\nNext time you try to login, provide your user_name!'.format(username)


def login(username):
    select_query = "SELECT id , user_name, phone_number, email, address FROM BaseUser WHERE user_name = ? LIMIT 1"
    db.query(select_query, [(username,)])
    user = db.c.fetchone()

    if user:
        my_user = BaseUser(user[0], user[1], user[2], user[3], user[4])
        select_query = "SELECT base_id FROM Client WHERE base_id = ?"
        db.query(select_query, [(my_user.get_id(),)])
        client = db.c.fetchone()
        if client:
            return Client(client[0])
        select_query = "SELECT base_id, title FROM Mechanic WHERE base_id = ?"
        db.query(select_query, [(my_user.get_id(),)])
        mechanic = db.c.fetchone()
        if mechanic:
            return Mechanic(select_query, [(mechanic[0], mechanic[1])])
        return client
    else:
        return False


def get_all_free_hours():
    select_query = "SELECT id , date, start_hour FROM Vehicle_repair WHERE vehicle IS NULL"
    db.query(select_query)
    query = db.c.fetchall()
    result = ''
    for item in query:
        if datetime.datetime.strptime(str(item[1]), '%d-%m-%Y') > datetime.datetime.now():
            result += '| ' + str(item[0]) + '  | ' + str(item[1]) + ' | ' + str(item[2]) + ' |\n'
    return result


def get_free_hours_by_id(id):
    select_query = "SELECT date, start_hour FROM Vehicle_repair WHERE id = ?"
    db.query(select_query, [(id,)])
    query = db.c.fetchall()
    result = ''
    for item in query:
        if datetime.datetime.strptime(str(item[0]), '%d-%m-%Y') > datetime.datetime.now():
            result += str(item[0]) + ' at ' + str(item[1])
    return result


def list_free_hours_date(date):
    select_query = "SELECT id, date, start_hour FROM Vehicle_repair WHERE date = ? AND vehicle IS NULL"
    db.query(select_query, [(date,)])
    query = db.c.fetchall()
    result = ''
    for item in query:
        if datetime.datetime.strptime(str(item[1]), '%d-%m-%Y') > datetime.datetime.now():
            result += str(item[2] + '\n')
    return result


def get_baseuserid_by_name(name):
    select_query = "SELECT id FROM BaseUser WHERE user_name = ?"
    db.query(select_query, [(name,)])
    query = db.c.fetchone()
    return query[0]


def add_vehicle(category, make, model, number, box, owner):
    insert_sql = "INSERT INTO Vehicle (category, make, model, register_number, gear_box, owner) VALUES (?, ?, ?, ?, ?, ?)"
    db.query(insert_sql, [(category, make, model, number, box, owner)])
    return 'Thank you! You added new personal vehicle!'


def get_all_vehicle():
    select_query = "SELECT id, make, model, register_number FROM Vehicle"
    db.query(select_query)
    return db.c.fetchall()


def get_all_service():
    select_query = "SELECT id, name FROM Service"
    db.query(select_query)
    return db.c.fetchall()


def choose_service_by_id(id):
    select_query = "SELECT name FROM Service WHERE id = ?"
    db.query(select_query, id)
    query = db.c.fetchone()
    return query[0]


def save_repair_hour(vehicle_id, service_id, update_date):
    update_query = "UPDATE Vehicle_repair SET vehicle = ?, mechanic_service = ? WHERE date = ?"
    db.query(update_query, [(vehicle_id, service_id, update_date)])


def get_vehicle_by_id(id):
    select_query = "SELECT make, model, register_number FROM Vehicle WHERE id = ?"
    db.query(select_query, [(id,)])
    query = db.c.fetchone()
    result = 'Vehicle: {} {} with RegNumber {}'.format(query[0], query[1], query[2])
    return result


def get_vehicle_date_by_id(id):
    select_query = "SELECT date FROM Vehicle_repair WHERE id = ?"
    db.query(select_query, [(id,)])
    query = db.c.fetchone()
    return query[0]


def update_repair_hour_by_id(id):
    print('Choose Date:')
    date = input()
    print('Choose Hour:')
    start_hour = input()

    update_query = "UPDATE Vehicle_repair SET start_hour = ?, date = ? WHERE id = ?"
    db.query(update_query, [(start_hour, date, id)])


def delete_repair_hour_by_id(id):
    delete_query = "DELETE FROM Vehicle_repair WHERE id = ?"
    db.query(delete_query, [(id,)])


def list_personal_vehicles(user_name):
    user_id = get_baseuserid_by_name(user_name)
    select_query = "SELECT category, make, model, register_number, gear_box FROM Vehicle WHERE owner = ?"
    db.query(select_query, [(user_id,)])
    query = db.c.fetchall()
    result = ''
    for item in query:
        result += str(item[0]) + ' ' + str(item[1]) + ' ' + str(item[2]) + ' ' + str(item[3]) + ' ' + str(item[4]) + '\n'
    return result


def update_vehicle(vehicle_id):
    print('Choose Category:')
    category = input()
    print('Choose Make:')
    make = input()
    print('Choose Model:')
    model = input()
    print('Choose Register Number:')
    register_number = input()
    print('Choose Gear Box:')
    gear_box = input()
    print('Choose Owner:')
    owner = input()
    update_query = "UPDATE Vehicle SET category = ?, make = ?, model = ?, register_number = ?, gear_box = ?, owner = ? WHERE id = ?"
    db.query(update_query, [(category, make, model, register_number, gear_box, owner, vehicle_id)])


def delete_vehicle(vehicle_id):
    delete_query = "DELETE FROM Vehicle WHERE id = ?"
    db.query(delete_query, [(vehicle_id,)])
