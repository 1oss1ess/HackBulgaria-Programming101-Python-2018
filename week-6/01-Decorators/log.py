import datetime

from functools import wraps

lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def log(file):
    def accepter(func):
        t1 = datetime.datetime.now()
        with open(file, 'a') as f:
            result = f.write('{} was called at {}\n'.format(func.__name__, t1))

        @wraps(func)
        def decorator(*args, **kwargs):
            return result
        return decorator
    return accepter


def encrypt(required):
    def accepter(func):
        @wraps(func)
        def decorator(*args, **kwargs):
            return result
        msg = func()
        result = ''
        for char in msg:
            if char == ' ':
                result += ' '
            for index, item in enumerate(lower_alphabet):
                if char in item:
                    result += lower_alphabet[index + required]
                elif char in upper_alphabet[index]:
                    result += upper_alphabet[index + required]
        return decorator
    return accepter


@log('log.txt')
@encrypt(2)
def get_low():
    return "Get get get low"


get_low()
