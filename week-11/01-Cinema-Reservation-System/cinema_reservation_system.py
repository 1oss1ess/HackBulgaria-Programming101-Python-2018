from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import func
from create_database import *
from movie import Movie
from user import User
from projection import Project
from reservation import Reservation


class Cinema_ctr:

    def __init__(self):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def show_movies_by_rating(self):
        movies = self.session.query(Movie).order_by(Movie.rating)
        print('|id|\t|name|\t|rating|')
        for movie in movies:
            print(movie)

    def show_movie_projections(self, movie_id, date=None):
        available = 100 - self.session.query(Reservation.projection_id).filter(Reservation.projection_id == movie_id).count()
        movie = self.session.query(Movie).filter(Movie.id == movie_id).first()
        if date is None:
            movies = self.session.query(Project.id, Project.type, func.date(Project.date), func.time(Project.time)).filter(Project.movie_id == movie_id).all()
        else:
            movies = self.session.query(Project.id, Project.type, func.date(Project.date), func.time(Project.time)).filter(Project.movie_id == movie_id).filter(Project.date == date).all()
        print("Projections for movie '{}:".format(movie.name))
        for movie in movies:
            print("[{}] - {} {} ({}) - {} spots available".format(movie[0], movie[2], movie[3], movie[1], available))

    def show_movies(self):
        print('Current movies:')
        movies_by_id = self.session.query(Movie).all()
        for movie in movies_by_id:
            print(movie)

    def show_projection_by_id(self, id):
        print('Available seats (marked with a dot):')
        reservations = self.session.query(Reservation.row, Reservation.col).filter(Reservation.projection_id == id).all()
        matrix = []
        for row in range(10):
            array = []
            for col in range(10):
                if (row + 1, col + 1) in reservations:
                    array.append('X')
                else:
                    array.append('.')
            matrix.append(array)
        self._show_seat(matrix)
        return matrix

    def _show_seat(self, hall_matrix):
        print("  " + (" ".join([str(i) for i in list(range(1, 10 + 1))])))
        iterator = 1
        for row in hall_matrix:
            print(str(iterator) + " " + (" ".join(row)))
            iterator += 1

    def make_reservation(self, hall, number_of_tickets, movie_id):
        reserved_seat = []
        iterator = 0
        number_of_choose_seat = 0
        while iterator < int(number_of_tickets):
            choose_seat = input('Step 4 (Seats): Choose seat %d>' % (number_of_choose_seat + 1))
            row, col = choose_seat.split(',')
            row = int(row.replace('(', ''))
            col = int(col.replace(')', ''))
            seat = (row, col)
            iterator += 1
            if seat > (10, 10):
                iterator -= 1
                print("Lol... NO!")
            elif hall[seat[0] - 1][seat[1] - 1] == 'X':
                iterator -= 1
                print('This seat is already taken!')
            else:
                reserved_seat.append(seat)
                hall[seat[0] - 1][seat[1] - 1] = 'X'

        self._show_reservation(reserved_seat, movie_id)
        return reserved_seat

    def _show_reservation(self, reserved_seat, movie_id):
        movie = self.session.query(Movie).filter(Movie.id == movie_id).first()
        print('Movie: {} ({})'.format(movie.name, movie.rating))
        projection = self.session.query(func.date(Project.date), func.time(Project.time)).filter(Project.movie_id == movie_id).first()
        print('Date and Time: {} ({})'.format(projection[0], projection[1]))
        print("Seats: %s" % (", ".join([str(seat) for seat in reserved_seat])))

    def confirm_reservation(self, user_id, projection_id, reserved_seat):
        confirmed = False
        while not confirmed:
            confirmation = input("Step 5 (Type 'finalize' to confirm or type 'reject' to reject) > ")

            if confirmation == "finalize":
                for seat in reserved_seat:
                    reservation = Reservation(user_id=user_id, projection_id=projection_id, row=seat[0], col=seat[1])
                    self.session.add(reservation)
                    self.session.commit()
                print('Thanks.')
                confirmed = True

            if confirmation == "reject":
                print("This reservation was rejected.")
                return True

    def cancel_reservation(self, name):
        project_id = input('Select which projection to cancel >')
        user_id = self.session.query(User.id).filter(User.username == name).first()
        user_reservations = self.session.query(Reservation.user_id, Reservation.projection_id, Reservation.row, Reservation.col).filter(Reservation.projection_id == project_id).filter(Reservation.user_id == user_id[0]).all()
        for row in user_reservations:
            print("[%d] - projection: %d, (%d, %d)" % row)
        delete_reservation = self.session.query(Reservation).filter(Reservation.projection_id == project_id).filter(Reservation.user_id == user_id[0])
        delete_reservation.delete(synchronize_session=False)
        self.session.commit()
        print('Your reservation is cancel')

    def help(self):
        help = ["Here is the list of commands (spells):",
                "   show movies - Shows all movies ordered by rating",
                "   show movie projections <movie_id> [<date>] - Shows all movies projections with given movie id and date - date is optional",
                "   make reservation - Interface for reservation",
                "   cancel reservation <name> - Cancels a reservation",
                "   exit - Exit of the program",
                "   help - This thing"]

        print("\n".join(help))

    def exit(self):
        print('Exit...')
