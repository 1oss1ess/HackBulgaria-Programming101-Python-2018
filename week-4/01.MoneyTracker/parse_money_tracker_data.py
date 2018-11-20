class ParseMoneyTrackerData:

    def __init__(self, data):
        self.data = data

    def parse_the_data(self):
        with open(self.data) as f:
            result = f.readlines()
        return result
