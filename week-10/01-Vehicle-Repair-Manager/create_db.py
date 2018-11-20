from mydatabase import MyDB
from queries import *

db = MyDB()

# db.query(DROP_BASE_USER_T)
# db.query(DROP_CLIENT_T)
# db.query(DROP_MECHANIC_T)
db.query(DROP_VEHICLE_T)
# db.query(DROP_SERVICE_T)
# db.query(DROP_MECHANIC_SERVICES_T)
# db.query(DROP_VEHICLE_REPAIR_T)

db.query(CREATE_BASE_USER_T)
db.query(CREATE_MECHANIC_T)
db.query(CREATE_CLIENT_T)
db.query(CREATE_VEHICLE_T)
db.query(CREATE_SERVICE_T)
db.query(CREATE_MECHANIC_SERVICES_T)
db.query(CREATE_VEHICLE_REPAIR_T)

data_user = [('Roza', 'roza@r.com', '088', 'Sofia')]
# data_mechanic = [('1', 'Gosho')]
# data_mechanic_service = [('1', '1')]
# data_vehicle = [('Automobile', 'Audi', 'A3', 'X 8888 XX', 'Manual', '1')]
# data_service1 = [('Oil Change', )]
# data_service2 = [('Tire Change', )]
# data_client = [('1', )]
# data_vehicle_repair = [('24-05-2018', '10:00', '1', '82.5', '1')]

db.query(INSERT_BASEUSER, data_user)
# db.query(INSERT_MECHANIC, data_mechanic)
# db.query(INSERT_MECHANIC_SERVICES, data_mechanic_service)
# db.query(INSERT_VEHICLE, data_vehicle)
# db.query(INSERT_SERVICE, data_service1)
# db.query(INSERT_SERVICE, data_service2)
# db.query(INSERT_CLIENT, data_client)
# db.query(INSERT_VEHICLE_REPAIR, data_vehicle_repair)
