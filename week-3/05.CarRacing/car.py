class Car:

    def __init__(self, car, model, max_speed):
        self.car = car
        self.model = model
        self.max_speed = max_speed

    def __str__(self):
        return "{} {}".format(self.car, self.max_speed)
