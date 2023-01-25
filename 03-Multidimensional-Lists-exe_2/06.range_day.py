def shoot_func(direction):
    r = my_position[0] + directions[direction][0]
    c = my_position[1] + directions[direction][1]

    while 0 <= r < size and 0 <= c < size:
        if field[r][c] == 'x':
            field[r][c] = '.'
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


def move_func(direction, steps):
    r = my_position[0] + (directions[direction][0] * steps)
    c = my_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < size and 0 <= c < size):
        return my_position

    if field[r][c] == 'x':
        return my_position

    return r, c


size = 5
field = []
total_targets = 0
shoot_targets = 0
my_position = [0, 0]
targets_position = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    field.append(input().split())

    if 'A' in field[row]:
        my_position = [row, field[row].index('A')]
        field[row][my_position[1]] = '.'

    if 'x' in field[row]:
        total_targets += field[row].count('x')

for _ in range(int(input())):
    command = input().split()

    if command[0] == 'shoot':
        target_pos = shoot_func(command[1])

        if target_pos:
            shoot_targets += 1
            targets_position.append(target_pos)

    elif command[0] == 'move':
        my_position = move_func(command[1], int(command[2]))

    if shoot_targets == total_targets:
        print(f'Training completed! All {total_targets} targets hit.')
        break

else:
    print(f'Training not completed! {total_targets - shoot_targets} targets left.')

[print(x) for x in targets_position]
