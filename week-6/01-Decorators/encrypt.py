lower_alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
                  'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
upper_alphabet = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                  'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']


def encrypt(required):
    def accpter(func):
        def decorator():
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
    return accpter


@encrypt(2)
def get_low():
    return "Get get get low"


print(get_low())
