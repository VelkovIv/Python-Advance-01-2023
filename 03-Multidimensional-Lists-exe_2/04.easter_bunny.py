field_size = int(input())
field = []

bunny_pos = []
max_num_eggs = 0
best_direction = None
best_path = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(field_size):
    field.append(input().split())

    if "B" in field[row]:
        bunny_pos = [row, field[row].index("B")]

for direction in directions:
    row, col = [
        bunny_pos[0] + directions[direction][0],
        bunny_pos[1] + directions[direction][1]
    ]
    num_of_eggs = 0
    path = []

    while 0 <= row < field_size and 0 <= col < field_size:
        if field[row][col] == "X":
            break

        num_of_eggs += int(field[row][col])
        path.append([row, col])

        row += directions[direction][0]
        col += directions[direction][1]

    if num_of_eggs >= max_num_eggs:
        max_num_eggs = num_of_eggs
        best_path = path
        best_direction = direction

print(best_direction)
print(*best_path, sep="\n")
print(max_num_eggs)
