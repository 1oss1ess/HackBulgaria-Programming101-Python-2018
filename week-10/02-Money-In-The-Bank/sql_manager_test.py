import sys
import unittest
import sql_manager

from sql_manager import *

sys.path.append("..")


class SqlManagerTests(unittest.TestCase):

    def setUp(self):
        sql_manager.create_clients_table()
        sql_manager.register('Tester', 'Password123123!', 'tester@mail.com')

    def test_sql_injections_fails(self):
        logged_user = sql_manager.login("' OR 1 = 1 --", 'password')
        self.assertFalse(logged_user)

    def test_register(self):
        sql_manager.cursor.execute('SELECT COUNT(*)  FROM clients WHERE username = %s AND password = %s', ('Dinko', hashed_pass('Dinko', 'Password123123!')))
        users_count_before = sql_manager.cursor.fetchone()

        sql_manager.register('Dinko', 'Password123123!', 'tester@mail.com')

        sql_manager.cursor.execute('SELECT COUNT(*)  FROM clients WHERE username = %s AND password = %s', ('Dinko', hashed_pass('Dinko', 'Password123123!')))
        users_count = sql_manager.cursor.fetchone()

        self.assertEqual(users_count[0], users_count_before[0] + 1)

    def test_login(self):
        logged_user = sql_manager.login('Tester', 'Password123123!')
        self.assertEqual(logged_user.get_username(), 'Tester')

    def test_login_wrong_password(self):
        logged_user = sql_manager.login('Tester', 'F123567')
        self.assertFalse(logged_user)

    def test_login_username_not_exist(self):
        logged_user = sql_manager.login('gosho', 'asd')
        self.assertFalse(logged_user)

    def test_password_hashed(self):
        password = 'Password123123!'
        hashed_password = sql_manager.hashed_pass('Tester', 'Password123123!')
        self.assertNotEqual(password, hashed_password)

    def test_change_message(self):
        logged_user = sql_manager.login('Tester', 'Password123123!')
        new_message = "podaivinototam"
        sql_manager.change_message(new_message, logged_user)
        self.assertEqual(logged_user.get_message(), new_message)

    def test_change_password(self):
        logged_user = sql_manager.login('Tester', 'Password123123!')
        new_password = "Qwerty!1"
        sql_manager.change_pass(new_password, logged_user)

        logged_user_new_password = sql_manager.login('Tester', new_password)
        self.assertEqual(logged_user_new_password.get_username(), 'Tester')


if __name__ == '__main__':
    unittest.main()
