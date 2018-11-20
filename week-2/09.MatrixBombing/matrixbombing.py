from itertools import product


def neighbours(cell, size):
    for c in product(*(range(n - 1, n + 2) for n in cell)):
        if c != cell and all(0 <= n < size for n in c):
            yield c


def matrix_bombing_plan(m):
    dictionary = {}
    current_sum_array = 0
    for row in range(0, len(m)):
        for col in range(0, len(m)):
            current_sum_array += m[row][col]
    for row in range(0, len(m)):
        for col in range(0, len(m)):
            bomb_sum = 0
            sum_arr = current_sum_array
            bombed = m
            coordinates = row, col
            bomb = bombed[row][col]
            neighbour_array = list(neighbours(coordinates, len(m)))
            for neighbour in neighbour_array:
                if m[neighbour[0]][neighbour[1]] >= bomb:
                    bomb_sum += bomb
                else:
                    bomb_sum += m[neighbour[0]][neighbour[1]]
            dictionary[coordinates] = sum_arr - bomb_sum

    return dictionary


print(matrix_bombing_plan([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
