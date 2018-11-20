def elevator_trips(people_weight, people_floors, elevator_floors,
                   max_people, max_weight):
    people_maxweight = []
    count_people = 0
    first_element = people_floors[0]
    elevator_trip = 0
    if elevator_floors > 0:
        elevator_trip += 1
    for index, element in enumerate(people_floors):
        print(first_element, element)
        if count_people < max_people and first_element <= element:
            count_people += 1
            people_maxweight.append(people_weight[index])
            first_element = element
            elevator_trip += 1
        else:
            print(sum(people_maxweight))
            people_maxweight = []
            count_people = 0
            people_maxweight.append(people_weight[index])
            elevator_trip += 1
            first_element = element
    print(sum(people_maxweight))
    print(elevator_trip)


elevator_trips([40, 40, 100, 80, 60], [2, 3, 3, 2, 3], 3, 5, 200)
print()
elevator_trips([80, 60, 40], [2, 3, 5], 5, 2, 200)
