class Driver:

    def __init__(self, name, car):
        self.name = name
        self.car = car

    def __str__(self):
        return "{}".format(self.name)

    def __eq__(self, other):
        return self.name == other
