def swap_elements_func(matrix_, coordinates):
    row1, col1, row2, col2 = coordinates
    matrix_[row1][col1], matrix_[row2][col2] = matrix_[row2][col2], matrix_[row1][col1]

    return matrix_


def check_func(indexes):
    if {indexes[0], indexes[2]}.issubset(valid_rows) and {indexes[1], cols < indexes[3]}.issubset(valid_cols):
        return True

    return False


def print_func(matrix_):
    for row in matrix_:
        for element in row:
            print(element, end=' ')
        print()


rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]

valid_rows = range(rows)
valid_cols = range(cols)

command, *data = input().split()
while command != 'END':
    indexes = [int(x) for x in data]

    check = check_func(indexes)

    if len(indexes) == 4 and command == 'swap' and check:
        sniffing_matrix = swap_elements_func(matrix, indexes)
        print_func(sniffing_matrix)
    else:
        print('Invalid input!')

    command, *data = input().split()
