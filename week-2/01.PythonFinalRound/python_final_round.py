def is_number_balanced(number):

    digits = [int(x) for x in str(number)]
    digits_len = len(digits)
    array_digits_left = []
    array_digits_right = []

    for i in range(0, digits_len // 2):
        array_digits_left.append(digits[i])
    if digits_len % 2 == 1:
        for i in range(digits_len // 2 + 1, digits_len):
            array_digits_right.append(digits[i])
    else:
        for i in range(digits_len // 2, digits_len):
            array_digits_right.append(digits[i])
    if sum(array_digits_right) == sum(array_digits_left):
        return True
    else:
        return False


def increasing_or_decreasing(seq):

    previous_digit = seq[0]
    array_of_digits_up = []
    array_of_digits_down = []
    array_of_digits_up.append(previous_digit)
    array_of_digits_down.append(previous_digit)

    for i in range(1, len(seq)):
        if previous_digit + 1 == seq[i]:
            array_of_digits_up.append(seq[i])
            previous_digit = seq[i]
        elif previous_digit - 1 == seq[i]:
            array_of_digits_down.append(seq[i])
            previous_digit = seq[i]

    if len(seq) == len(array_of_digits_up) and seq[0] + 1 == seq[1]:
        return "Up!"
    elif len(seq) == len(array_of_digits_down) and seq[0] - 1 == seq[1]:
        return "Down!"
    else:
        return False


def get_largest_palindrome(number):
    while True:
        number -= 1
        if str(number) == str(number)[::-1]:
            return number


def sum_of_numbers(n):

    digit = ""
    array = []

    for i in n:
        if i.isdigit():
            digit += i
        else:
            array.append(digit)
            digit = ""
    array.append(digit)
    digits = sum([int(j) for j in array if j.isdigit()])
    return digits


def birthday_ranges(birthdays, ranges):
    result = []
    for day in ranges:
        if day[0] in range(1, 365 + 1) and day[1] in range(1, 365 + 1):
            count = 0
            for birthday in birthdays:
                if birthday in range(1, 365 + 1) and birthday in range(day[0], day[1] + 1):
                    count += 1
            result.append(count)

    return result


def numbers_to_message(pressed_sequence):
    dictionary = {
        2: ['a', 'b', 'c'],
        3: ['d', 'e', 'f'],
        4: ['g', 'h', 'i'],
        5: ['j', 'k', 'l'],
        6: ['m', 'n', 'o'],
        7: ['p', 'q', 'r', 's'],
        8: ['t', 'u', 'v'],
        9: ['w', 'x', 'y', 'z']
    }

    number = pressed_sequence
    current_item = number[0]
    count = 0
    array_count = []
    array_number = []
    for index in number:
        if current_item == index:
            count += 1
        else:
            array_number.append(current_item)
            array_count.append(count)
            current_item = index
            count = 1
    array_number.append(current_item)
    array_count.append(count)

    msg = ""
    is_upper = False
    for index, item in enumerate(array_number, start=0):
        if item == 0:
            msg += " "
        elif is_upper:
            counter = array_count[index] % len(dictionary[item])
            msg += dictionary[item][counter - 1].upper()
            is_upper = False
        elif item == 1:
            is_upper = True
        elif item == -1:
            continue
        else:
            counter = array_count[index] % len(dictionary[item])
            msg += dictionary[item][counter - 1]
    return msg


def message_to_numbers(message):
    diction = {
        'abc': 2,
        'def': 3,
        'ghi': 4,
        'jkl': 5,
        'mno': 6,
        'pqrs': 7,
        'tuv': 8,
        'wxyz': 9
    }

    sms = []

    array_text = message

    for arr_text in array_text:
        if arr_text[0] == " ":
            sms.append(0)
        elif arr_text[0].isupper():
            sms.append(1)
        my_text = arr_text[0].lower()

        for index, char in enumerate(diction, start=2):
            if my_text in char:
                for text in arr_text:
                    count_char = char.index(text.lower())
                    if len(sms) > 0 and index == sms[-1]:
                        sms.append(-1)
                    while count_char >= 0:
                        sms.append(index)
                        count_char -= 1
    return sms


def elevator_trips(people_weight, people_floors, elevator_floors, max_people, max_weight):
    list_1 = []
    count = 0
    if (len(people_weight) == 0) or (len(people_floors) == 0):
        return count
    for i in range(len(people_weight)):
        if i == 0:
            if elevator_floors > 0:
                count += 1
            list_1.append(people_weight[i])
            count += 1
        else:
            if people_floors[i] == people_floors[i - 1] and sum(list_1) + people_weight[i] <= max_weight and max_people >= len(list_1) + 1:
                list_1.append(people_weight[i])
            else:
                if sum(list_1) + people_weight[i] <= max_weight and max_people >= len(list_1) + 1:
                    count += 1
                    list_1.append(people_weight[i])
                else:
                    list_1 = [people_weight[i]]
                    count += 2
    return count
