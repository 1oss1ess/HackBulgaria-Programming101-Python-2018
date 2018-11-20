import hashlib

from sqlalchemy.orm import sessionmaker
from create_database import *
from user import User


class User_ctr:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def hashed_pass(self, username, password):
        hash = hashlib.pbkdf2_hmac(
            'sha256',
            password.encode(),
            username.encode(),
            10000
        ).hex()
        return str(hash)

    def register(self, username, password):
        hash_password = self.hashed_pass(username, password)
        user = User(username=username, password=hash_password)
        self.session.add(user)
        self.session.commit()

    def login(self, username, password):
        hash_password = self.hashed_pass(username, password)
        user = self.session.query(User).filter(User.username == username).filter(User.password == hash_password).first()
        if type(user) is User:
            return user
        else:
            False

    def user_exists(self, user=None):
        check_users = self.session.query(User).filter(User.username == user).first()
        if type(check_users) is User:
            print('Hello, {}'.format(user))
            return True
        else:
            print('Wrong username or password!')
            return False
