def matrix_input_read_func():
    rows, columns = map(int, input().split(', '))
    matrix = []

    for row in range(rows):
        current_row = list(map(int, input().split(' ')))
        matrix.append(current_row)

    return matrix


def sum_of_columns_func(matrix):
    for col in range(len(matrix[0])):
        sum_of_column = 0
        for row in range(len(matrix)):
            sum_of_column += matrix[row][col]

        print(sum_of_column)


data = matrix_input_read_func()
sum_of_columns_func(data)
