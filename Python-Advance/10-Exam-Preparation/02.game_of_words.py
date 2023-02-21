initial_string = input()
size = int(input())

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
player_pos = []
field = []

for row in range(size):
    field.append(list(input()))

    if "P" in field[row]:
        player_pos = [row, field[row].index("P")]
        field[row][player_pos[1]] = "-"

commands_num = int(input())

for i in range(commands_num):
    command = input()
    new_pos = player_pos[0] + moves[command][0], player_pos[1] + moves[command][1]

    if not (0 <= new_pos[0] < size) or not (0 <= new_pos[1] < size):
        initial_string = initial_string[:-1]
        continue

    if field[new_pos[0]][new_pos[1]] != "-":
        initial_string += field[new_pos[0]][new_pos[1]]
        field[new_pos[0]][new_pos[1]] = "-"

    player_pos = new_pos
field[player_pos[0]][player_pos[1]] = "P"

print(initial_string)
for row in range(size):
    print("".join(field[row]))