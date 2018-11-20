import math


def sum_of_digits(n):
    if n < 0:
        n *= -1
    result = sum([int(number) for number in str(n)])
    return result


def to_digits(n):
    result = [int(number) for number in str(n)]
    return result


def to_number(digits):
    num = int(''.join(map(str, digits)))
    return num


def fact_digits(n):
    result = 0
    list_of_numbers = to_digits(n)
    for number in list_of_numbers:
        result += math.factorial(number)
    return result


def fibonacci(n):
    result = []
    number1 = 0
    number2 = 1
    for i in range(1, n + 1):
        sum_of_number = number1 + number2
        result.append(sum_of_number)
        if i > 1:
            number1 = number2
            number2 = sum_of_number
    return result


def fib_number(n):
    fibonacci_numbers = fibonacci(n)
    return to_number(fibonacci_numbers)


def palindrome(n):
    text = str(n)
    if text == text[::-1]:
        return True
    else:
        return False


def count_vowels(str):
    vowels = "aeiouy"
    result = sum([True for text in str.lower() if text in vowels])
    return result


def count_consonants(str):
    consonants = "bcdfghjklmnpqrstvwxz"
    result = sum([True for text in str.lower() if text in consonants])
    return result


def char_histogram(string):
    count_char = {}
    count = 0
    for index in string:
        count += 1
        if index in count_char:
            count_char[index] = count
        else:
            count = 1
            count_char[index] = count
    return count_char
