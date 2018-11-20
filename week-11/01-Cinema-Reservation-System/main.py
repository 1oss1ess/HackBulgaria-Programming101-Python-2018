import getpass
from cinema_reservation_system import Cinema_ctr
from user_controller import User_ctr
from create_database import *


def menu():
    print("Welcome to our cinema reservation system.\nEnter 'help' for usage hints")
    create_db()
    user = User_ctr()
    cinema = Cinema_ctr()
    while True:
        command = input('>')
        if command == 'register':
            username = input('Your username: ')
            password = input('Your password: ')
            user.register(username, password)

        elif command == 'show movies':
            cinema.show_movies()

        elif command.startswith('show movie projections'):
            command_array = command.split(' ')
            if len(command_array) == 4:
                movie_id = command_array[-1]
                cinema.show_movie_projections(movie_id)
            elif len(command_array) == 5:
                movie_id = command_array[-2]
                movie_date = command_array[-1]
                cinema.show_movie_projections(movie_id, movie_date)

        elif command == 'make reservation':
            print('You need to a user in the system to make reservations!')
            username = input('Username: ')
            password = getpass.getpass('Password: ')
            my_user = user.login(username, password)
            if user.user_exists(my_user.get_name()):
                number_of_tickets = input('Step 1 (User): Choose number of tickets>')
                cinema.show_movies()

                movie_id = input('Step 2 (Movie): Choose a movie>')
                cinema.show_movie_projections(movie_id)

                projection = input('Step 3 (Projection): Choose a projection>')
                hall = cinema.show_projection_by_id(projection)
                reserved_seat = cinema.make_reservation(hall, number_of_tickets, movie_id)
                cinema.confirm_reservation(my_user.get_id(), projection, reserved_seat)

        elif command == 'cancel reservation':
            username = input('Username: ')
            password = getpass.getpass('Password: ')
            my_user = user.login(username, password)
            if user.user_exists(my_user.get_name()):
                cinema.cancel_reservation(my_user.get_name())

        elif command == 'help':
            cinema.help()

        elif command == 'exit':
            cinema.exit()
            break


menu()
