import json


class Championship:

    def __init__(self, name, race_count):
        self.name = name
        self.race_count = race_count

    def top3(self):
        count = 0
        top3_driver = []
        with open('result.json', 'r') as outfile:
            my_file = json.load(outfile)
            for item in my_file:
                count += 1
                if count > 4:
                    for index in item:
                        if self.race_count > 0:
                            self.race_count -= 1
                            top3_driver.append(index)
        return top3_driver
