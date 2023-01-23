
def count_matrix_2x2_func(matrix_):
    counter = 0

    for row in range(len(matrix_) - 1):
        for col in range(len(matrix_[row]) - 1):

            if matrix_[row][col] == matrix_[row][col + 1]:
                if matrix_[row][col] == matrix_[row + 1][col] == matrix_[row + 1][col + 1]:
                    counter += 1

    return counter


rows, cols = map(int, input().split())
matrix = [input().split() for _ in range(rows)]
matrix_counter = count_matrix_2x2_func(matrix)
print(matrix_counter)
