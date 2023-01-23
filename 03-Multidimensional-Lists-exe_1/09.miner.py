from collections import deque

size_of_square_field = int(input())
commands = deque(input().split())
field = [[el for el in input().split()] for _ in range(size_of_square_field)]

# instead of function all moves are in dictionary
command = {
    "left": (0, -1),
    "right": (0, 1),
    "up": (-1, 0),
    "down": (1, 0)
}

coals = 0
start_position = []
game_over = False

# find all coals in the field and start position for mining
for row in range(size_of_square_field):
    for col in range(len(field[row])):
        if field[row][col] == "c":
            coals += 1
        if field[row][col] == 's':
            start_position.append(row)
            start_position.append(col)

while commands:
    current_command = commands.popleft()

    next_move = command[current_command]
    next_position = start_position
    # check validity of next position
    if 0 <= (start_position[0] + next_move[0]) < len(field):
        next_position = (start_position[0] + next_move[0], next_position[1])
    if 0 <= (start_position[1] + next_move[1]) < len(field):
        next_position = (next_position[0], start_position[1] + next_move[1])

    if field[next_position[0]][next_position[1]] == "c":
        coals -= 1
        field[next_position[0]][next_position[1]] = "*"
    elif field[next_position[0]][next_position[1]] == 'e':
        game_over = True
        break
    start_position = next_position

if game_over:
    print(f"Game over! ({next_position[0]}, {next_position[1]})")
elif coals == 0:
    print(f"You collected all coal! ({next_position[0]}, {next_position[1]})")
else:
    print(f"{coals} pieces of coal left. ({next_position[0]}, {next_position[1]})")
