from sqlalchemy import create_engine
from movie import Movie as Base_movie
from projection import Project as Base_project
from user import User as Base_user
from reservation import Reservation as Base_reservation

engine = create_engine('sqlite:///cinema.db')


def create_db():
    Base_movie.metadata.create_all(engine)
    Base_project.metadata.create_all(engine)
    Base_user.metadata.create_all(engine)
    Base_reservation.metadata.create_all(engine)
