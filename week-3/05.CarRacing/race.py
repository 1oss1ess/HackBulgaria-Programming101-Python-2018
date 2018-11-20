import random
import json


class Race:

    def __init__(self, drivers, crash_chance=random.uniform(0, 1)):
        self.drivers = drivers
        self.crash_chance = crash_chance

    def __eq__(self, other):
        return self.crash_chance == other

    def __hash__(self):
        return hash(self.crash_chance)

    def __lt__(self, other):
        return self.crash_chance < other

    def __getitem__(self, index):
        return self.drivers[index]

    def result(self):
        my_file = 'result.json'
        finish_driver = []
        crashed_driver = []
        array_of_chance = []
        add_text = {}
        race_points = 8
        for driver in self.drivers:
            crashed_chance_driver = random.uniform(0, self.crash_chance)
            if crashed_chance_driver < 0.55:
                array_of_chance.append(round(crashed_chance_driver, 2))
                finish_driver.append((round(crashed_chance_driver, 2), driver))
            else:
                crashed_driver.append("Unfortunately, {} has crashed.".format(str(driver)))

        array_of_chance.sort()

        for chance in array_of_chance[::-1]:
            for index, result in enumerate(finish_driver):
                if chance == result[0]:
                    if race_points < 4:
                        race_points = 0
                        add_text[str(result[1])] = race_points
                        finish_driver.pop(index)
                    else:
                        add_text[str(result[1])] = race_points
                        finish_driver.pop(index)
                        race_points -= 2

        add_text['crashed'] = crashed_driver

        with open(my_file, 'w') as fp:
            json.dump(add_text, fp, indent=4)

        return my_file
