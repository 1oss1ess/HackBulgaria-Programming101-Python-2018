import sys
from random import randint


def generate_numbers(filename, numbers):
    with open(filename, 'w') as file:
        for num in range(numbers):
            result = randint(num, 1000)
            file.write(str(result) + ' ')


def main():
    generate_numbers('numbers.txt', 100)


if __name__ == '__main__':
    main()
