def matrix_input_read_func():
    rows, columns = map(int, input().split(', '))
    matrix = []

    for row in range(rows):
        current_row = list(map(int, input().split(', ')))
        matrix.append(current_row)

    return matrix


data = matrix_input_read_func()
sum_of_matrix_elements = 0

for row in range(len(data)):
    sum_of_matrix_elements += sum(data[row])

print(sum_of_matrix_elements)
print(data)