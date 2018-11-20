from car import Car
from driver import Driver
from race import Race
from championship import Championship
import json

drivers = []
names = []
total = []
arr_driver = []
add_champion = {}
with open('cars.json', 'r') as outfile:
    file_car = json.load(outfile)
    for file in file_car['people']:
        car = Car(file['car'], file['model'], file['max_speed'])
        drivers.append(Driver(file['name'], car))
        names.append(file['name'])

my_race = Race(drivers)
champion = Championship("rage", 3)
names.append('crashed')
drivers = []
for count in range(champion.race_count):
    race = "Race #" + str(count + 1)
    drivers.append(race)
    drivers.append("###### START ######")
    result_champion = my_race.result()
    add_champion[str(champion.name)] = result_champion

    for champ_k, champ_v in add_champion.items():
        with open(champ_v, 'r') as outfile:
            file_champ = json.load(outfile)
            for name in names:
                if name in file_champ and name != 'crashed':
                    drivers.append(name + " - " + str(file_champ[name]))
                    # print(name, file_champ[name])
                    total.append((name, file_champ[name]))
                elif name in file_champ and name == 'crashed':
                    for crash in file_champ[name]:
                        drivers.append(crash)
                        # print(crash)
    arr_driver.append(drivers)
    drivers = []


arr_driver.append("Total championship {}:".format(champion.name))

my_set_drivers = {x[0] for x in total}
result_drivers = [(i, sum(x[1] for x in total if x[0] == i)) for i in my_set_drivers]
sorted_drivers = sorted(result_drivers, key=lambda tup: tup[1])

arr_driver.append(sorted_drivers[::-1])
with open('result.json', 'w') as fp:
    json.dump(arr_driver, fp, indent=4)
