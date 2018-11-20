DROP_BASE_USER_T = 'DROP TABLE IF EXISTS BaseUser'
DROP_CLIENT_T = 'DROP TABLE IF EXISTS Client'
DROP_MECHANIC_T = 'DROP TABLE IF EXISTS Mechanic'
DROP_VEHICLE_T = 'DROP TABLE IF EXISTS Vehicle'
DROP_SERVICE_T = 'DROP TABLE IF EXISTS Service'
DROP_MECHANIC_SERVICES_T = 'DROP TABLE IF EXISTS Mechanic_services'
DROP_VEHICLE_REPAIR_T = 'DROP TABLE IF EXISTS Vehicle_repair'

CREATE_BASE_USER_T = """
    CREATE TABLE IF NOT EXISTS BaseUser (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_name TEXT NOT NULL,
        email TEXT NOT NULL,
        phone_number INTEGER NOT NULL,
        address TEXT NOT NULL
    )
"""

CREATE_CLIENT_T = '''
    CREATE TABLE IF NOT EXISTS Client (
        base_id INTEGER UNIQUE NOT NULL,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    )
'''

CREATE_MECHANIC_T = '''
    CREATE TABLE IF NOT EXISTS Mechanic (
        base_id INTEGER UNIQUE NOT NULL,
        title TEXT NOT NULL,
        FOREIGN KEY(base_id) REFERENCES BaseUser(id)
    )
'''

CREATE_VEHICLE_T = """
    CREATE TABLE IF NOT EXISTS Vehicle (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        category TEXT NOT NULL,
        make TEXT NOT NULL,
        model TEXT NOT NULL,
        register_number TEXT NOT NULL,
        gear_box TEXT NOT NULL,
        owner INTEGER,
        FOREIGN KEY(owner) REFERENCES BaseUser(id)
    )
"""

CREATE_SERVICE_T = """
    CREATE TABLE IF NOT EXISTS Service (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    )
"""

CREATE_MECHANIC_SERVICES_T = """
    CREATE TABLE IF NOT EXISTS Mechanic_services (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        mechanic_id INTEGER NOT NULL,
        service_id INTEGER NOT NULL,
        FOREIGN KEY(mechanic_id) REFERENCES Mechanic(base_id),
        FOREIGN KEY(service_id) REFERENCES Service(id)
    )
"""

CREATE_VEHICLE_REPAIR_T = '''
    CREATE TABLE IF NOT EXISTS Vehicle_repair (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        date TEXT,
        start_hour TEXT,
        vehicle INTEGER,
        bill REAL,
        mechanic_service INTEGER,
        FOREIGN KEY(vehicle) REFERENCES Vehicle(id),
        FOREIGN KEY(mechanic_service) REFERENCES MechanicService(id)
    )
'''
INSERT_BASEUSER = '''
    INSERT INTO BaseUser (
        user_name, email,
        phone_number,
        address)
        VALUES(?, ?, ?, ?)
'''

INSERT_MECHANIC = '''
    INSERT INTO Mechanic (
        base_id,
        title)
        VALUES(?, ?)
'''

INSERT_MECHANIC_SERVICES = '''
    INSERT INTO Mechanic_services (
        mechanic_id,
        service_id)
        VALUES(?, ?)
'''

INSERT_SERVICE = '''
    INSERT INTO Service (
        name)
        VALUES(?)
'''

INSERT_VEHICLE = '''
    INSERT INTO Vehicle (
        category,
        make,
        model,
        register_number,
        gear_box,
        owner)
        VALUES(?, ?, ?, ?, ?, ?)
'''

INSERT_CLIENT = '''
    INSERT INTO Client (
        base_id)
        VALUES(?)
'''

INSERT_VEHICLE_REPAIR = '''
    INSERT INTO Vehicle_repair (
        date,
        start_hour,
        vehicle,
        bill,
        mechanic_service
        )
        VALUES(?, ?, ?, ?, ?)
'''
