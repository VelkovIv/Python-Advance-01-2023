def matrix_input_read_func():
    rows = int(input())
    matrix = []

    for row in range(rows):
        current_row = list(map(int, input().split(', ')))
        matrix.append(current_row)

    return matrix


data = matrix_input_read_func()
flattering_matrix = []

for row in range(len(data)):
    for col in range(len(data[row])):
        flattering_matrix.append(data[row][col])

print(flattering_matrix)