def find_sub_matrix_3x3_func(matrix_, size):
    sub_matrix_data = [0, 0, 0]
    rows_ = len(matrix_) - size + 1
    cols = len(matrix_[0]) - size + 1

    for row in range(rows_):
        for col in range(cols):

            current_sum = matrix_[row][col] + matrix_[row][col + 1] + matrix_[row][col + 2] + \
                          matrix_[row + 1][col] + matrix_[row + 1][col + 1] + matrix_[row + 1][col + 2] + \
                          matrix_[row + 2][col] + matrix_[row + 2][col + 1] + matrix_[row + 2][col + 2]

            if current_sum > sub_matrix_data[0]:
                sub_matrix_data[0] = current_sum
                sub_matrix_data[1] = row
                sub_matrix_data[2] = col

    return sub_matrix_data


rows, columns = map(int, input().split())
matrix = [[int(el) for el in input().split()] for _ in range(rows)]
sub_matrix_size = 3
sub_matrix = find_sub_matrix_3x3_func(matrix, sub_matrix_size)

print(f'Sum = {sub_matrix[0]}')
rows_ = sub_matrix[1]
cols = sub_matrix[2]
for r in range(rows_, rows_ + sub_matrix_size):
    for c in range(cols, cols + sub_matrix_size):
        print(matrix[r][c], end=' ')
    print()



