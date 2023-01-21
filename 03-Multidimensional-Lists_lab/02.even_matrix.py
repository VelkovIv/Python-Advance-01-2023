def matrix_input_read_func():
    rows = int(input())
    matrix_input = []

    for row in range(rows):
        current_row = list(map(int, input().split(', ')))
        current_entry = [el for el in current_row if el % 2 == 0]
        matrix_input.append(current_entry)

    return matrix_input


matrix = matrix_input_read_func()
print(matrix)

