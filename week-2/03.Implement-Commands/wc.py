import sys


def read_file(arguments):
    with open(arguments) as f:
        result = f.read()
        return result


def num_chars(text):
    count_chars = sum([1 for char in text])
    return count_chars


def num_words(text):
    count_words = sum([1 for word in text.split()])
    return count_words


def num_lines(text):
    count = sum([1 for line in text if '\n' in line])
    return count


def main():
    command = sys.argv[1]
    text = read_file(sys.argv[2])

    if command == 'chars':
        print(num_chars(text))
    elif command == 'words':
        print(num_words(text))
    elif command == 'lines':
        print(num_lines(text))


if __name__ == '__main__':
    main()
