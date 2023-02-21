field_size = int(input())
field = []

collected_tea_bags = 0
alice_pos = []

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(field_size):
    field.append(input().split())

    if "A" in field[row]:
        alice_pos = [row, field[row].index("A")]
        field[row][alice_pos[1]] = "*"

while collected_tea_bags < 10:
    current_direction = input()

    row, col = [
        alice_pos[0] + directions[current_direction][0],
        alice_pos[1] + directions[current_direction][1]
    ]

    if not (0 <= row < field_size and 0 <= col < field_size):
        break

    position = field[row][col]
    field[row][col] = "*"

    if position.isdigit():
        collected_tea_bags += int(position)

    if position == "R":
        break

    alice_pos = [row, col]

if collected_tea_bags >= 10:
    print("She did it! She went to the party.")
else:
    print("Alice didn't make it to the tea party.")

for row in field:
    print(" ".join(row))
