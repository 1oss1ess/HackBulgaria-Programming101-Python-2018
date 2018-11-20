from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    password = Column(String)

    def get_name(self):
        return self.username

    def get_id(self):
        return self.id

    def __str__(self):
        return "|{}|  |{}|".format(self.id, self.username)

    def __repr__(self):
        return self.__str__()
