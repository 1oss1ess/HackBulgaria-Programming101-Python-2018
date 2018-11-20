from mydatabase import MyDB


db = MyDB()


def update_repair_hour(id):
    while True:
        select_query = "SELECT date, start_hour, bill, vehicle FROM Vehicle_repair WHERE id = ?"
        db.query(select_query, id)
        query = db.c.fetchone()

        current_bill = str(query[2])
        current_start_hour = str(query[1])
        vehicle = str(query[3])
        result = ''
        result += 'On ' + str(query[0]) + ' at ' + current_start_hour + ':\n'

        select_query = "SELECT user_name FROM BaseUser WHERE id = ?"
        db.query(select_query, vehicle)
        query = db.c.fetchone()
        result += 'Client: ' + str(query[0]) + '\n'

        select_query = "SELECT make, model FROM Vehicle WHERE id = ?"
        db.query(select_query, vehicle)
        query = db.c.fetchone()
        result += 'Vehicle: ' + str(query[0]) + ' ' + str(query[1]) + '\n'
        print(result)
        print('Choose one of the following:\n1 - change start hour\n2 - change bill\n3 - return to main menu')
        command = input('>>> ')
        if command == '1':
            print('Current Start Hour is: {}'.format(current_start_hour))
            print('New Start Hour:')
            command = input('>>> ')
            update_query = "UPDATE Vehicle_repair SET start_hour = ? WHERE id = ?"
            db.query(update_query, [(command, id)])
        elif command == '2':
            print('Current Bill is: {}\nNew Bill:'.format(current_bill))
            command = input('>>> ')
            update_query = "UPDATE Vehicle_repair SET bill = ? WHERE id = ?"
            db.query(update_query, [(command, id)])
        elif command == '3':
            break


def add_new_repair_hour():
    print('Repair hour date:')
    repair_date = input('>>> ')
    print('Start Hour:')
    repair_hour = input('>>> ')
    insert_query = "INSERT INTO Vehicle_repair (date, start_hour) VALUES (?, ?)"
    db.query(insert_query, [(repair_date, repair_hour)])

    select_query = "SELECT id, date, start_hour FROM Vehicle_repair"
    db.query(select_query)
    query = db.c.fetchall()
    result = '| id | date | start_hour   |\n'
    for item in query:
        result += '| ' + str(item[0]) + '  | ' + str(item[1]) + '  | ' + str(item[2]) + ' |\n'
    print(result)


def add_new_service():
    command = input('Provide New service name:')
    insert_query = "INSERT INTO Service (name) VALUES (?)"
    db.query(insert_query, [(command,)])


def list_busy_hours_date(date):
    select_query = "SELECT id, start_hour FROM Vehicle_repair WHERE date = ? AND  vehicle NOT NULL"
    db.query(select_query, [(date,)])
    query = db.c.fetchall()
    result = '| id | start_hour   |\n'
    for item in query:
        result += '| ' + str(item[0]) + '  | ' + str(item[1]) + '  |\n'
    return result


def list_all_busy_hours():
    select_query = "SELECT id, start_hour FROM Vehicle_repair WHERE vehicle NOT NULL"
    db.query(select_query)
    query = db.c.fetchall()
    result = '| id | start_hour   |\n'
    for item in query:
        result += '| ' + str(item[0]) + '  | ' + str(item[1]) + '  |\n'
    return result


def list_free_hours_date(date):
    select_query = "SELECT id, start_hour FROM Vehicle_repair WHERE date = ? AND vehicle IS NULL"
    db.query(select_query, [(date,)])
    query = db.c.fetchall()
    result = '| id | start_hour   |\n'
    for item in query:
        result += '| ' + str(item[0]) + '  | ' + str(item[1]) + '  |\n'
    return result


def list_all_free_hours():
    select_query = "SELECT id, start_hour FROM Vehicle_repair WHERE vehicle IS NULL"
    db.query(select_query)
    query = db.c.fetchall()
    result = '| id | start_hour   |\n'
    for item in query:
        result += '| ' + str(item[0]) + '  | ' + str(item[1]) + '  |\n'
    return result
