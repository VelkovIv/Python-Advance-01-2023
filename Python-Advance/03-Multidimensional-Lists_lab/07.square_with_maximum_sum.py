def matrix_input_read_func():
    rows, columns = map(int, input().split(', '))
    matrix = []

    for _ in range(rows):
        current_row = list(map(int, input().split(', ')))
        matrix.append(current_row)

    return matrix


def find_bigger_sub_matrix(matrix, matrix_size):
    max_matrix_sum = [0, 0, 0]
    rows = len(matrix) - matrix_size + 1
    cols = len(matrix[0]) - matrix_size + 1
    for row in range(rows):
        for col in range(cols):
            total_sum = 0
            total_sum += matrix[row][col] + matrix[row][col + 1] + matrix[row + 1][col] + matrix[row + 1][col + 1]
            if total_sum > max_matrix_sum[0]:
                max_matrix_sum[0] = total_sum
                max_matrix_sum[1] = row
                max_matrix_sum[2] = col

    return max_matrix_sum


def print_func(matrix, sub_matrix_info, size):
    rows = sub_matrix_info[1]
    cols = sub_matrix_info[2]
    for row in range(rows, rows + size):
        for col in range(cols, cols + size):
            print(matrix[row][col], end=" ")
        print()
    print(sub_matrix_info[0])


data = matrix_input_read_func()
sub_matrix_size = 2
sub_matrix_data = find_bigger_sub_matrix(data, sub_matrix_size)
print_func(data, sub_matrix_data, sub_matrix_size)
