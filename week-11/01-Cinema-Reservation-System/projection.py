from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, Time
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

from movie import Movie

Base = declarative_base()


class Project(Base):
    __tablename__ = 'projections'
    id = Column(Integer, primary_key=True)
    movie_id = Column(Integer, ForeignKey(Movie.id))
    type = Column(String)
    date = Column(Date)
    time = Column(Time)
    movie = relationship(Movie, backref='projections')

    def __str__(self):
        return "|{}|  |{}|  |{}|  |{}|  |{}|".format(self.id, self.movie_id, self.type, self.date, self.time)

    def __repr__(self):
        return self.__str__()
