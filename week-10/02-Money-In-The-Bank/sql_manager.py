import re
import hashlib
import psycopg2
import smtplib
import random
import string
from datetime import datetime, timedelta
from client import Client
from requirement_password import *
from setings import *


conn = psycopg2.connect(dbname="bank")
cursor = conn.cursor()


def drop_tables():
    drop_query_tan_codes = 'DROP TABLE tan_codes'
    cursor.execute(drop_query_tan_codes)
    conn.commit()
    drop_query_clients = 'DROP TABLE clients'
    cursor.execute(drop_query_clients)
    conn.commit()


def create_clients_table():
    create_query = '''create table if not exists
                clients(id SERIAL PRIMARY KEY,
                username VARCHAR(128),
                password VARCHAR(128),
                balance REAL DEFAULT 0,
                message TEXT,
                timeban TIMESTAMP DEFAULT NOW(),
                email VARCHAR(128),
                countfaillogin NUMERIC DEFAULT 0)'''

    cursor.execute(create_query)
    conn.commit()


def create_tan_table():
    create_tan = '''CREATE TABLE IF NOT EXISTS
                tan_codes (id SERIAL PRIMARY KEY,
                tancode VARCHAR(128),
                user_id INT,
                 FOREIGN KEY (user_id) REFERENCES clients (id))'''

    cursor.execute(create_tan)
    conn.commit()


def is_strong_the_password(username, password):
    pass_not_count_user = username not in password
    long_symbol = re.search(IS_EIGHT_SYMBOL, password)
    special_symbol = re.search(IS_SPECIAL_SYMBOL, password)
    digit = re.search(IS_DIGIT, password)
    upperdase = re.search(IS_UPPERCASE_LETTER, password)

    if long_symbol and special_symbol and digit and upperdase and pass_not_count_user:
        return True
    return False


def change_message(new_message, logged_user):
    update_sql = "UPDATE clients SET message = %s WHERE id = %s"
    cursor.execute(update_sql, (new_message, logged_user.get_id()))
    conn.commit()
    logged_user.set_message(new_message)


def change_pass(new_pass, logged_user):
    new_password = hashed_pass(logged_user.get_username(), new_pass)
    update_sql = "UPDATE clients SET password = %s WHERE id = %s"
    cursor.execute(update_sql, (new_password, logged_user.get_id()))
    conn.commit()


def hashed_pass(username, password):
    hash = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        username.encode(),
        10000
    ).hex()
    return str(hash)


def register(username, password, email):
    if is_strong_the_password(username, password):
        insert_sql = "INSERT INTO clients (username, password, email) VALUES (%s, %s, %s)"
        hash_password = hashed_pass(username, password)
        cursor.execute(insert_sql, (username, hash_password, email))
        conn.commit()

        return SUCCSESSFULL_REG
    else:
        return INCORRECT_PASS


def countfunc(username):
    count_query = 'SELECT countfaillogin FROM clients WHERE username = %s'
    cursor.execute(count_query, (username,))
    count = cursor.fetchone()[0]

    update_count_query = 'UPDATE clients SET countfaillogin = %s WHERE username = %s'
    cursor.execute(update_count_query, (count + 1, username))
    conn.commit()

    count_query = 'SELECT countfaillogin FROM clients WHERE username = %s'
    cursor.execute(count_query, (username, ))
    count = cursor.fetchone()
    return count[0]


def login(username, password):
    hash_password = hashed_pass(username, password)

    select_query = "SELECT id FROM clients WHERE username = %s LIMIT 1"
    cursor.execute(select_query, (username, ))
    user = cursor.fetchone()
    if user is None:
        print('username is not exist')
        return False

    select_query = "SELECT id, username, balance, message, email FROM clients WHERE username = %s AND password = %s LIMIT 1"

    cursor.execute(select_query, (username, hash_password))
    user = cursor.fetchone()
    if(user):
        return Client(user[0], user[1], user[2], user[3], user[4])
    else:
        count = countfunc(username)
        if count == 3:
            count = 0
            ban_query = 'UPDATE clients SET timeban = %s, countfaillogin = %s WHERE username = %s'
            cursor.execute(ban_query, (datetime.now() + timedelta(seconds=300), count, username))
            conn.commit()
        return False


def update_reset_pass(password, username):
    update_query = 'UPDATE clients SET password = %s WHERE username = %s'
    cursor.execute(update_query, (password, username))
    conn.commit()


def generate_random_string():
    random_str = ''.join([random.choice(string.ascii_letters + string.digits) for n in range(32)])
    return random_str


def send_reset_email(username, email):
    random_password = generate_random_string()
    new_password = hashed_pass(username, random_password)
    update_reset_pass(new_password, username)
    gmail_user = GMAIL_USER
    gmail_pass = GMAIL_PASS
    from_user = GMAIL_USER
    to_user = email
    subject = 'reseting the password for the bank $$$ money comming!!!'
    text = 'Your new pass is: {}'.format(random_password)
    message = '''\From: %s\nTo: %s\nSubject: %s\n\n%s''' % (from_user, ', '.join(to_user), subject, text)
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(gmail_user, gmail_pass)
        server.sendmail(from_user, to_user, message)
        server.quit()
        print('successfully send the mail')
    except ValueError:
        print('failed to send mail')


def generate_tan():
    array_tan = []
    for index in range(0, 10):
        random_str = ''.join([random.choice(string.digits + string.ascii_letters.lower()) for n in range(64)])
        array_tan.append(random_str)
    return array_tan


def get_tan(username, email):
    tan_code = generate_tan()
    select_user = 'SELECT id FROM clients WHERE username = %s'
    cursor.execute(select_user, (username, ))
    user_id = cursor.fetchone()
    select_tan = 'SELECT COUNT(tancode) FROM tan_codes INNER JOIN clients ON tan_codes.user_id = clients.id WHERE clients.username = %s'
    cursor.execute(select_tan, (username, ))
    if cursor.fetchone()[0] == 0:
        for index_of_tan in tan_code:
            update_tan = 'INSERT INTO tan_codes (tancode, user_id) VALUES (%s, %s)'
            cursor.execute(update_tan, (index_of_tan, user_id))
            conn.commit()
        gmail_user = GMAIL_USER
        gmail_pass = GMAIL_PASS
        from_user = GMAIL_USER
        to_user = email
        subject = 'your tan code for the bank'
        text = 'Your tan codes: is:\n{}'.format('\n'.join(tan_code))
        message = '''\From: %s\nTo: %s\nSubject: %s\n\n%s''' % (from_user, ', '.join(to_user), subject, text)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(gmail_user, gmail_pass)
            server.sendmail(from_user, to_user, message)
            server.quit()
            print('successfully send the mail with your code')
        except ValueError:
            print('failed to send mail')
    else:
        print('You have code check the email')


def get_balance(username):
    get_user_balance = 'SELECT balance FROM clients WHERE username = %s'
    cursor.execute(get_user_balance, (username,))
    return float(cursor.fetchone()[0])


def deposit(username, deposit_sum):
    try:
        deposit_sum = float(deposit_sum)
        if deposit_sum < 0:
            return '''
                        failed to deposit
                        '''
        elif deposit_sum > 0:
            tan = input('Enter TAN code: ')
            select_tan = 'SELECT tancode FROM tan_codes INNER JOIN clients ON tan_codes.user_id = clients.id WHERE clients.username = %s AND tan_codes.tancode = %s'
            cursor.execute(select_tan, (username, tan))
            if cursor.fetchone() is not None:
                delete_tan = 'DELETE FROM tan_codes WHERE tancode = %s'
                cursor.execute(delete_tan, (tan,))
                conn.commit()
                balance = get_balance(username)
                new_balance = balance + deposit_sum
                update_deposit_query = 'UPDATE clients SET balance = %s WHERE username = %s'
                cursor.execute(update_deposit_query, (new_balance, username))
                conn.commit()
                print('Transaction successful!')
                return '{} were deposited to the bank'.format(deposit_sum)
            else:
                return 'You entered wrong code!'
    except ValueError:
        return 'You entered not a number!'


def withdraw(username, withdraw_sum):
    balance = get_balance(username)
    try:
        withdraw_sum = float(withdraw_sum)
        if withdraw_sum < 0:
            return '''
                        You cann't withdraw negarive amount
                        '''
        elif withdraw_sum > 0:
            if withdraw_sum > balance:
                return 'Not enought money!'
            else:
                new_balance = balance - withdraw_sum
                update_withdraw_query = 'UPDATE clients SET balance = %s WHERE username = %s'
                cursor.execute(update_withdraw_query, (new_balance, username))
                conn.commit()
                return 'Successfull withdraw: {}\nNew balance: {}'.format(withdraw_sum, new_balance)
    except ValueError:
        print('You entered not a number!')
