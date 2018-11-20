from parse_money_tracker_data import ParseMoneyTrackerData

file = 'money_tracker.txt'

parse_file = ParseMoneyTrackerData(file)
result = parse_file.parse_the_data()
print(result)
