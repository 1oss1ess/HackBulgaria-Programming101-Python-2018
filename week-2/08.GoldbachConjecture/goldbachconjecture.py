import math


def is_prime(n):
    if n % 2 == 0 and n > 2:
        return False
    return all(n % i for i in range(3, int(math.sqrt(n)) + 1, 2))


def goldbach(n):
    result = []
    simple_numbers = [number for number in range(2, n + 1) if is_prime(number)]

    for i in simple_numbers:
        for j in simple_numbers:
            if i + j == n:
                if (j, i) not in result:
                    result.append((i, j))

    return result
