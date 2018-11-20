import csv


def read_file_csv(file):
    array_of_rows = []
    # current_arr = []
    with open(file) as f:
        reader = csv.reader(f)
        for row in reader:
            # for i in row:
            #     current_arr.append(str(i).strip())
            # print(str(row[4]).strip())
            result = str(row).split(", '")
            array_of_rows.append(result)
    return array_of_rows


file_read = read_file_csv('test_data.csv')


def filter_by_full_name(file_read, full_name):
    result = [row for row in file_read if full_name in str(row)]
    return result


def filter_by_fname_and_color(file_read, full_name, favourite_color):
    search_by_fname = filter_by_full_name(file_read, full_name)
    result = [row for index, row in enumerate(search_by_fname) if favourite_color == str(search_by_fname[index][1]).replace("'", '').strip()]
    return result


def startswith_fname(file_read, full_name__starswith):
    result = [row for index, row in enumerate(file_read) if str(file_read[index][0]).replace('[', '').replace("'", '').strip().split(' ')[0] == full_name__starswith]
    return result


def contains_email(file_read, email__contains):
    matching = [row for row in file_read if email__contains in str(row)]
    return matching


def filter_by_salary(file_read, salary__gt, salary__lt):
    matching = [row for index, row in enumerate(file_read) if index > 0 and int(salary__gt) < int(file_read[index][-1].replace(" '", '').replace("']", '')) and int(salary__lt) > int(file_read[index][-1].replace(" '", '').replace("']", ''))]
    return matching


def order_by(file_read, salary__gt, salary__lt, order_by):
    find_index = 0
    for file_index, file_element in enumerate(file_read[0]):
        if order_by in file_element:
            find_index = file_index

    my_arr = []
    array_salary = filter_by_salary(file_read, salary__gt, salary__lt)

    for salary in array_salary:
        my_arr.append(tuple(salary))

    return sorted(my_arr, key=lambda x: x[find_index])


def filter(file_read, **kwargs):
    full_name = []
    favourite_color = []
    company_name = []
    email = []
    phone_number = []
    salary = []
    order_by_words = []
    for key in kwargs:
        if key.startswith("full_name"):
            full_name.append(kwargs[key])
        elif key.startswith("favourite_color"):
            favourite_color.append(kwargs[key])
        elif key.startswith("company_name"):
            company_name.append(kwargs[key])
        elif key.startswith("email"):
            email.append(kwargs[key])
        elif key.startswith("phone_number"):
            phone_number.append(kwargs[key])
        elif key.startswith("salary"):
            salary.append(kwargs[key])
        elif key.startswith("order_by"):
            order_by_words.append(kwargs[key])
    if len(full_name) == 1 and len(favourite_color) == 0 and " " in full_name[0]:
        return filter_by_full_name(file_read, full_name[0])
    elif len(full_name) == 1 and len(favourite_color) == 1:
        return filter_by_fname_and_color(file_read, full_name[0], favourite_color[0])
    elif len(full_name) == 1 and " " not in full_name[0]:
        return startswith_fname(file_read, full_name[0])
    elif len(email) == 1:
        return contains_email(file_read, email[0])
    elif len(salary) > 1 and len(order_by_words) == 0:
        return filter_by_salary(file_read, salary[0], salary[1])
    elif len(order_by_words) == 1:
        return order_by(file_read, salary[0], salary[1], order_by_words[0])
