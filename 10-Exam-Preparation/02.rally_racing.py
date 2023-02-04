size_of_field = int(input())
racing_number = input()
tunel_positions = []
car_position = [0, 0]
kilometers = 0
finish = False

directions = {
    'left': (0, -1),
    'right': (0, 1),
    "up": (-1, 0),
    'down': (1, 0)
}

matrix = []
for row in range(size_of_field):
    matrix.append(list(input().split()))

    if 'T' in matrix[row]:
        tunel_positions.append([row, matrix[row].index('T')])

direction = input()
while direction != 'End':
    car_position[0] += directions[direction][0]
    car_position[1] += directions[direction][1]
    # kilometers += 10

    if matrix[car_position[0]][car_position[1]] == '.':
        kilometers += 10
    elif matrix[car_position[0]][car_position[1]] == 'T':
        matrix[car_position[0]][car_position[1]] = '.'
        for i in range(len(tunel_positions)):
            if car_position == tunel_positions[i]:
                tunel_positions.pop(i)
                break

        car_position = tunel_positions[0]
        matrix[tunel_positions[0][0]][tunel_positions[0][1]] = '.'
        tunel_positions.pop(0)
        kilometers += 30

    elif matrix[car_position[0]][car_position[1]] == 'F':
        kilometers += 10
        finish = True
        break

    direction = input()

matrix[car_position[0]][car_position[1]] = 'C'

if finish:
    print(f'Racing car {racing_number} finished the stage!')
else:
    print(f'Racing car {racing_number} DNF.')

print(f'Distance covered {kilometers} km.')
for row in matrix:
    print(''.join(row))
