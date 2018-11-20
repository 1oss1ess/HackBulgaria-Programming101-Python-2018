def is_credit_card_valid(number):
    is_valid_card = False
    number = str(number)

    if len(number) % 2 == 1:
        odd_number = [int(num) * 2 for index, num in enumerate(number[::-1])
                      if index % 2 == 1]

        result = sum([int(num) for index, num in enumerate(
            number[::-1]) if index % 2 == 0])

        result += sum([int(num) for num in str(odd_number) if num.isdigit()])

        if result % 10 == 0:
            is_valid_card = True
    return is_valid_card
