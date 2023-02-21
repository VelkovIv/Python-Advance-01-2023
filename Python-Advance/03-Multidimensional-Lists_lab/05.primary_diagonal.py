def matrix_input_read_func():
    rows = int(input())
    matrix = []

    for row in range(rows):
        current_row = list(map(int, input().split(' ')))
        matrix.append(current_row)

    return matrix


data = matrix_input_read_func()
primary_diagonal = 0

for i in range(len(data)):
    primary_diagonal += data[i][i]

print(primary_diagonal)