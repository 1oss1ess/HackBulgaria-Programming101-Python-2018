import sys


def sum_number(arguments):
    with open(arguments) as f:
        result = f.read()
        result = result.split()
        return sum([int(num) for num in result])


def main():
    print(sum_number('numbers.txt'))


if __name__ == '__main__':
    main()
