def matrix_input_read_func():
    rows = int(input())
    matrix = []

    for row in range(rows):
        current_row = list(input())
        matrix.append(current_row)

    return matrix


def check_symbol_in_matrix(matrix, symbol):
    for r in range(len(matrix)):
        for c in range(len(matrix[r])):
            if matrix[r][c] == symbol:
                return r, c

def print_func(matrix, symbol):
    result = check_symbol_in_matrix(matrix,symbol)
    if result:
        print(result)
    else:
        print(f'{symbol} does not occur in the matrix')


data = matrix_input_read_func()
symbol_to_find = input()
print_func(data, symbol_to_find)
