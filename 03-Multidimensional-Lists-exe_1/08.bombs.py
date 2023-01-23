def bomb_detonation_func(matrix_, row, col):
    bomb_power = matrix_[row][col]
    matrix_[row][col] = 0
    row_start = row if row == 0 else row - 1
    col_start = col if col == 0 else col - 1
    row_end = row + 1 if row == len(matrix_) - 1 else row + 2
    col_end = col + 1 if col == len(matrix_[0]) - 1 else col + 2

    for i in range(row_start, row_end):
        for y in range(col_start, col_end):
            if matrix_[i][y] > 0:
                matrix_[i][y] -= bomb_power

    return matrix_


def print_func(matrix_):
    alive_cells = 0
    matrix_sum = 0

    for row in range(len(matrix_)):
        for col in range(len(matrix_[row])):
            if matrix_[row][col] > 0:
                alive_cells += 1
                matrix_sum += matrix_[row][col]

    print(f'Alive cells: {alive_cells}')
    print(f'Sum: {matrix_sum}')

    for row in matrix_:
        for col in row:
            print(col, end=' ')
        print()


rows = int(input())
matrix = [[int(el) for el in input().split()] for i in range(rows)]
bombs = input().split()

for bomb in bombs:
    r, c = bomb.split(',')

    bomb_detonation_func(matrix, int(r), int(c))

print_func(matrix)
