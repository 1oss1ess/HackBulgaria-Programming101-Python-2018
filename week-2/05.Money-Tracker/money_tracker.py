def list_user_data(all_user_data):
    with open(all_user_data) as f:
        result = f.read()
    return result


def show_user_incomes(all_user_data):
    result = 0
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        number = index.split(', ')[0]
        text = index.split(', ' and ' ')[-1]
        if text.startswith("Income"):
            result += int(number)
    return result


def show_user_savings(all_user_data):
    result = 0
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        number = index.split(', ')[0]
        text = index.split(', ' and ' ')[-1]
        if text.startswith("Income"):
            result += float(number)
        elif text.startswith("Expense"):
            result = round(float(result) - float(number), 2)
    return result


def show_user_deposits(all_user_data):
    result = 0
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        number = index.split(', ')[0]
        if len(index.split(', ')) > 1:
            text = index.split(', ')[1]

            if text.startswith("Deposit"):
                result += round(float(number), 2)
    return result


def show_user_expenses(all_user_data):
    result = 0
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        number = index.split(', ')[0]
        text = index.split(', ' and ' ')[-1]
        if text.startswith("Expense"):
            result = float(result) + float(number)
    return result


def list_user_expenses_ordered_by_categories(all_user_data):
    words_categories_expenses = ""
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        expense = index.split(', ' and ' ')[-1]
        text = index.split(', ')
        if expense.startswith("Expense"):
            if words_categories_expenses == "":
                words_categories_expenses = text[1]
            else:
                words_categories_expenses += ", " + text[1]
    words = words_categories_expenses.split(", ")
    words.sort()
    return words


def show_user_data_per_date(date, all_user_data):
    result = ""
    start_index = ""
    end_index = ""
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        text = index.split(', ' and ' ')
        if len(text) > 1 and date == text[1]:
            start_index = index.split(', ' and ' ')[0]
            end_index = index.split(', ' and ' ')[-1]
        elif len(text) > 1 and start_index == index.split(', ' and ' ')[0] and end_index == index.split(', ' and ' ')[-1] and date != text[1]:
            break
        elif start_index != "" and end_index != "":
            if result == "":
                result = index
            else:
                result += "\n" + index
    return result


def list_income_categories(all_user_data):
    words_categories_expenses = ""
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        expense = index.split(', ' and ' ')[-1]
        text = index.split(', ')
        if expense.startswith("Income"):
            if words_categories_expenses == "":
                words_categories_expenses = text[0] + " " + text[1]
            else:
                words_categories_expenses += ", " + text[0] + " " + text[1]
    words = words_categories_expenses.split(", ")
    return words


def list_expense_categories(all_user_data):
    words_categories_expenses = ""
    string_split = list_user_data(all_user_data).split('\n')
    for index in string_split:
        expense = index.split(', ' and ' ')[-1]
        text = index.split(', ')
        if expense.startswith("Expense"):
            if words_categories_expenses == "":
                words_categories_expenses = text[0] + " " + text[1]
            else:
                words_categories_expenses += ", " + text[0] + " " + text[1]
    words = words_categories_expenses.split(", ")
    return words


def add_income(income_category, money, date, all_user_data):
    add_text = str(money) + ", " + income_category + ", New Income\n"
    string_split = list_user_data(all_user_data).split('\n')
    start_index = ""
    end_index = ""
    count = 0

    my_date = "=== " + date + " ==="
    if my_date not in string_split:
        count = 1
        f = open(all_user_data, "a+")
        new_date = my_date + "\n"
        f.write(new_date)
        f.write(add_text)
        f.close()

    for index in range(len(string_split)):
        if date in string_split[index]:
            start_index = string_split[index].split(', ' and ' ')[0]
            end_index = string_split[index].split(', ' and ' ')[-1]
        elif(start_index == string_split[index].split(', ' and ' ')[0]) and (end_index == string_split[index].split(', ' and ' ')[-1]) and count == 0:
            count = 1
            f = open(all_user_data, "r")
            oline = f.readlines()
            oline.insert(index, add_text)
            f.close()

            f = open(all_user_data, "w")
            f.writelines(oline)
            f.close()
        elif start_index != "" and index + 1 == len(string_split) and count == 0:
            count = 1
            f = open(all_user_data, "r")
            oline = f.readlines()
            oline.insert(index, add_text)
            f.close()

            f = open(all_user_data, "w")
            f.writelines(oline)
            f.close()


def add_expense(expense_category, money, date, all_user_data):
    add_text = str(money) + ", " + expense_category + ", New Expense\n"
    string_split = list_user_data(all_user_data).split('\n')
    start_index = ""
    end_index = ""
    count = 0

    my_date = "=== " + date + " ==="
    if my_date not in string_split:
        count = 1
        f = open(all_user_data, "a+")
        new_date = my_date + "\n"
        f.write(new_date)
        f.write(add_text)
        f.close()

    for index in range(len(string_split)):
        if date in string_split[index]:
            start_index = string_split[index].split(', ' and ' ')[0]
            end_index = string_split[index].split(', ' and ' ')[-1]
        elif(start_index == string_split[index].split(', ' and ' ')[0]) and (end_index == string_split[index].split(', ' and ' ')[-1]) and count == 0:
            count = 1
            f = open(all_user_data, "r")
            oline = f.readlines()
            oline.insert(index, add_text)
            f.close()

            f = open(all_user_data, "w")
            f.writelines(oline)
            f.close()
        elif start_index != "" and index + 1 == len(string_split) and count == 0:
            count = 1
            f = open(all_user_data, "r")
            oline = f.readlines()
            oline.insert(index, add_text)
            f.close()

            f = open(all_user_data, "w")
            f.writelines(oline)
            f.close()


# all_user_data = ''
# date = ''
# income_category = ''
# money = ''
# expense_category = ''
# while True:
#     print('Choose one of the following options to continue: ')
#     print('1 - show all data')
#     print('2 - show data for specific date')
#     print('3 - show expenses, ordered by categories')
#     print('4 - add new income')
#     print('5 - add new expense')
#     print('6 - exit')
#     userChoice = int(input())
#     if userChoice is 1:
#         print(list_user_data("money_tracker.txt"))
#     elif userChoice is 2:
#         show_user_data_per_date(date, all_user_data)
#     elif userChoice is 4:
#         while True:
#             print("New income amount:")
#             money = int(input())
#             print("New income type:")
#             income_category = str(input())
#             print("New income date:")
#             date = str(input())
#             if money != 0 and income_category != "" and date != "":
#                 break
#         add_income(income_category, money, date, "money_tracker.txt")
#     elif userChoice is 5:
#         add_expense(expense_category, money, date, all_user_data)
#     elif userChoice is 6:
#         break

add_expense("Food", 5, "24-03-2018", "money_tracker.txt")
# add_income("Deposit", 22, "23-03-2018", "money_tracker.txt")
