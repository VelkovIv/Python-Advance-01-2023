size = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(size)]

while True:
    current_input = input().split()

    if current_input[0] == "END":
        break

    command, row, col, value = current_input[0], int(current_input[1]), int(current_input[2]), int(current_input[3])

    if not (0 <= row < size and 0 <= col < size):
        print('Invalid coordinates')

    else:
        if command == "Add":
            matrix[row][col] += value
        elif command == "Subtract":
            matrix[row][col] -= value

[print(*row) for row in matrix]