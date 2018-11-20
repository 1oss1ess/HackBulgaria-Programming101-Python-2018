import user_controller
import mechanic_controller
from queries import *
from mydatabase import MyDB
from client import Client
from mechanic import Mechanic


class Menu:

    def client_menu(self, user_name):
        return 'Hello, {}!\nYou can choose from the following commands:\nlist_all_free_hours\nlist_free_hours <date>\nsave_repair_hour <hour_id>\nupdate_repair_hour <hour_id>\ndelete_repair_hour <hour_id>\nlist_personal_vehicles\nadd_vehicle\nupdate_vehicle <vehicle_id>\ndelete_vehicle <vehicle_id>\nexit'.format(user_name)

    def mechanic_menu(self, user_name):
        return 'Hello, {}!\nYou can choose from the following commands:\nlist_all_free_hours\nlist_free_hours <date>\nlist_all_busy_hours\nlist_busy_hours <date>\nadd_new_repair_hour\nadd_new_service\nupdate_repair_hour <hour_id>\nexit'.format(user_name)

    def is_client(self, user_name):
        while True:
            command = input('command> :')

            if command == 'list_all_free_hours':
                result = user_controller.get_all_free_hours()
                if result is not '':
                    print('| id | date | start_hour  |')
                    print(result)
                else:
                    print("There's no free hours")
                print(self.client_menu(user_name))
            elif command.startswith('list_free_hours'):
                date = command.split(' ')
                date = date[-1]
                print(user_controller.list_free_hours_date(date))
                print(self.client_menu(user_name))
            elif command == 'add_vehicle':
                category = input('Vehicle category:\n')
                make = input('Vehicle make:\n')
                model = input('Vehicle model:\n')
                number = input('Vehicle register number:\n')
                box = input('Vehicle gear box:\n')
                owner = user_controller.get_baseuserid_by_name(user_name)
                print(user_controller.add_vehicle(category, make, model, number, box, owner))
                print(self.client_menu(user_name))
            elif command.startswith('save_repair_hour'):
                id = command.split(' ')
                update_date_id = id[1]
                id = id[-1]
                save_repair_hour = user_controller.get_free_hours_by_id(id)
                print('Choose Vehicle to repair:\n')
                result = user_controller.get_all_vehicle()
                print('| id |               Vehicle              |')
                for item in result:
                    print('| ' + str(item[0]) + ' | ' + str(item[1]) + ' ' + str(item[2]) + ' with RegNumber: ' + str(item[3]) + ' |')
                choose_vehicle_id = input()
                print('Choose Service:')
                result = user_controller.get_all_service()
                print('| id |               Service              |')
                for item in result:
                    print('| ' + str(item[0]) + '  | ' + str(item[1]) + ' |')
                service_id = input()
                choose_service = user_controller.choose_service_by_id(service_id)
                update_date = user_controller.get_vehicle_date_by_id(update_date_id)
                user_controller.save_repair_hour(choose_vehicle_id, service_id, update_date)
                vehicle = user_controller.get_vehicle_by_id(choose_vehicle_id)
                print('Thank you! You saved an hour on ' + str(save_repair_hour) + ' for ' + str(choose_service + '\n' + str(vehicle)))
            elif command.startswith('update_repair_hour'):
                hour_id = command.split(' ')
                hour_id = hour_id[-1]
                user_controller.update_repair_hour_by_id(hour_id)
                print(self.client_menu(user_name))
            elif command.startswith('delete_repair_hour'):
                hour_id = command.split(' ')
                hour_id = hour_id[-1]
                user_controller.delete_repair_hour_by_id(hour_id)
                print(self.client_menu(user_name))
            elif command == 'list_personal_vehicles':
                print(user_controller.list_personal_vehicles(user_name))
                print(self.client_menu(user_name))
            elif command.startswith('update_vehicle'):
                vehicle_id = command.split(' ')
                vehicle_id = vehicle_id[-1]
                user_controller.update_vehicle(vehicle_id)
                print(self.client_menu(user_name))
            elif command.startswith('delete_vehicle'):
                vehicle_id = command.split(' ')
                vehicle_id = vehicle_id[-1]
                user_controller.delete_vehicle(vehicle_id)
                print(self.client_menu(user_name))
            elif command == 'exit':
                break
            else:
                print("Not a valid command")

    def is_mechanic(self, user_name):
        while True:
            command = input('command> :')
            if command.startswith('update_repair_hour'):
                id = command.split(' ')
                id = id[-1]
                mechanic_controller.update_repair_hour(id)
                print(self.mechanic_menu(user_name))
            elif command == 'add_new_repair_hour':
                mechanic_controller.add_new_repair_hour()
                print(self.mechanic_menu(user_name))
            elif command == 'add_new_service':
                mechanic_controller.add_new_service()
                print(self.mechanic_menu(user_name))
            elif command.startswith('list_busy_hours'):
                date = command.split(' ')
                date = date[-1]
                print(mechanic_controller.list_busy_hours_date(date))
                print(self.mechanic_menu(user_name))
            elif command == 'list_all_busy_hours':
                print(mechanic_controller.list_all_busy_hours())
                print(self.mechanic_menu(user_name))
            elif command.startswith('list_free_hours'):
                date = command.split(' ')
                date = date[-1]
                print(mechanic_controller.list_free_hours_date(date))
                print(self.mechanic_menu(user_name))
            elif command == 'list_all_free_hours':
                print(mechanic_controller.list_all_free_hours())
                print(self.mechanic_menu(user_name))
            elif command == 'exit':
                break

    def create_table(self):
        db = MyDB()
        db.query(CREATE_BASE_USER_T)
        db.query(CREATE_CLIENT_T)
        db.query(CREATE_MECHANIC_T)
        db.query(CREATE_VEHICLE_T)
        db.query(CREATE_SERVICE_T)
        db.query(CREATE_MECHANIC_SERVICES_T)
        db.query(CREATE_VEHICLE_REPAIR_T)

    def start(self):
        self.create_table()
        user_name = input('Hello!\nProvide your user_name:\n>>> ')
        user = user_controller.login(user_name)
        if type(user) is Client:
            print(self.client_menu(user_name))
            self.is_client(user_name)
        elif type(user) is Mechanic:
            print(self.mechanic_menu(user_name))
            self.is_mechanic(user_name)
        else:
            print('Unknown user!\n Would you like to create new user?')
            print(user_controller.register())


m = Menu()
m.start()
