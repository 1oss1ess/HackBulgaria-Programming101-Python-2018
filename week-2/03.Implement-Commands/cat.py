def cat(arguments):
    with open(arguments) as f:
        result = f.read()
    return result


def main():
    print(cat('file.txt'))


if __name__ == '__main__':
    main()
