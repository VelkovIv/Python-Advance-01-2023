size = 6

matrix = []
position = [0, 0]
moves = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

for _ in range(size):
    matrix.append(list(input().split()))

position_data = input()
position[0] = int(position_data[1:2])
position[1] = int(position_data[4:5])

command, *data = input().split(', ')
while command != 'Stop':

    position[0] += moves[data[0]][0]
    position[1] += moves[data[0]][1]

    if command == 'Create' and matrix[position[0]][position[1]] == '.':
        matrix[position[0]][position[1]] = data[1]

    elif command == 'Update' and matrix[position[0]][position[1]] != '.':
        matrix[position[0]][position[1]] = data[1]

    elif command == 'Delete' and matrix[position[0]][position[1]]!= '.':
        matrix[position[0]][position[1]] = '.'

    elif command == 'Read' and matrix[position[0]][position[1]]!= '.':
        print(matrix[position[0]][position[1]])

    command, *data = input().split(', ')

for row in range(size):
    print(" ".join(matrix[row]))