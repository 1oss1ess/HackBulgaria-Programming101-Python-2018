from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from projection import Project
from user import User

Base = declarative_base()


class Reservation(Base):
    __tablename__ = 'reservations'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey(User.id))
    projection_id = Column(Integer, ForeignKey(Project.id))
    row = Column(Integer)
    col = Column(Integer)
    user = relationship(User, backref='reservations')
    projection = relationship(Project, backref='reservations')

    def __str__(self):
        return "|{}|  |{}|".format(self.id, self.user_id, self.projection_id, self.row, self.col)

    def __repr__(self):
        return self.__str__()
