import sys


def cat2(arguments):
    with open(arguments[0]) as text1, open(arguments[1]) as text2:
        read_text1 = text1.read()
        read_text2 = text2.read()
        return read_text1 + '\n' + read_text2


def main():
    print(cat2(['file1.txt', 'file2.txt']))


if __name__ == '__main__':
    main()
