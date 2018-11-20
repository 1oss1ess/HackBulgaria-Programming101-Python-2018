def count_substrings(haystack, needle):
    return haystack.count(needle)


def sum_matrix(m):
    sum_array = 0
    for row in m:
        sum_array += sum(row)
    return sum_array


def nan_expand(times):
    my_string = 'NaN'
    add_string = 'Not a '
    result = ""
    if times > 0:
        result = result + add_string * times + my_string + result
    else:
        result += result
    return result


def prime_factorization(n):
    count = 0
    divisor = 2
    array = []
    number = n
    while n > 1:
        if n % divisor == 0:
            count += 1
            n //= divisor
        elif number != n:
            number = n
            array.append((divisor, count))
            divisor += 1
            count = 0
        else:
            divisor += 1
            count = 0
    array.append((divisor, count))
    return array


def group(list_of_things):
    array = []
    result_array = []
    num1 = list_of_things[0]
    num2 = 0
    for x in list_of_things:
        if x == 0:
            array.append(num1)
        else:
            num2 = x
            if num1 == num2:
                array.append(num1)
            else:
                num1 = num2
                result_array.append(array)
                array = []
                array.append(num1)
    result_array.append(array)
    return result_array


def max_consective(items):
    count = 1
    current_count = 0
    current_index = items[0]
    for index in items:
        if current_index == index:
            count += 1
        else:
            if current_count < count:
                current_count = count
            count = 1
            current_index = index

    if current_count < count:
        current_count = count
    return current_count


def all_rows_cols_diagonals(matrix):
    max_col = len(matrix)
    max_row = len(matrix[0])
    cols = [[] for i in range(max_col)]
    rows = [[] for i in range(max_row)]
    fdiag = [[] for i in range(max_col + max_row - 1)]
    bdiag = [[] for i in range(len(fdiag))]
    min_bdiag = -max_col + 1

    for index_col in range(max_col):
        for index_row in range(max_row):
            cols[index_col].append(matrix[index_col][index_row])
            rows[index_row].append(matrix[index_col][index_row])
            fdiag[index_row + index_col].append(
                matrix[index_col][index_row])
            bdiag[-min_bdiag + index_row - index_col].append(
                matrix[index_col][index_row])
    return cols, rows, fdiag, bdiag


def search_word(word, array):
    count = 0
    for index in array:
        current_word = ''.join(str(char) for char in index)
        reversed_word = ''.join(str(e) for e in index[::-1])
        if word in current_word:
            count += 1
        if word in reversed_word and word != word[::-1]:
            count += 1
    return count


def word_count():
    word = input()
    num_input = input()
    count_word = 0

    matrix = []
    num = num_input.split()
    num_row, num_col = int(num[0]), int(num[1])

    if num_row < len(word) and num_col < len(word):
        return 'Invalid number of rows or columns!'
    else:
        for row in range(0, num_row):
            rows_input = input()
            matrix.append(list(rows_input.split()))

        cols, rows, fdiag, bdiag = all_rows_cols_diagonals(matrix)

        count_word += search_word(word, cols)
        count_word += search_word(word, rows)
        count_word += search_word(word, fdiag)
        count_word += search_word(word, bdiag)
    return count_word


def gas_stations(distance, tank_size, stations):
    stations_len = len(stations)
    short_distances = []
    first_station = stations[0]
    size = tank_size
    last_station = stations[len(stations) - 1]
    for index in range(1, stations_len, 1):
        if stations[index] >= tank_size:
            short_distances.append(stations[index - 1])
            tank_size = size
            tank_size += first_station
        if distance - stations[index] > size and \
                last_station == stations[index + 1]:
            short_distances.append(stations[index + 1])
        first_station = stations[index]
    return sorted(short_distances)
