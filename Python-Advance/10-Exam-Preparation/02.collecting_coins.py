size = int(input())

total_coins = 0
player_pos = []
field = []
path = []
moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}
# creating field for player
for row in range(size):
    field.append(list(input().split()))

    if 'P' in field[row]:
        player_pos = [row, int(field[row].index('P'))]
        field[row][player_pos[1]] = 0

# path.append(player_pos)  # record path of the player

while True:
    command = input()
    path.append(player_pos)  # record path of the player
    new_pos = [player_pos[0] + moves[command][0], player_pos[1] + moves[command][1]]

    if new_pos[0] < 0:
        new_pos[0] = size - 1
    elif new_pos[0] > size - 1:
        new_pos[0] = 0

    if new_pos[1] < 0:
        new_pos[1] = size - 1
    elif new_pos[1] > size - 1:
        new_pos[1] = 0

    player_pos = new_pos

    if field[new_pos[0]][new_pos[1]] == "X":
        total_coins = int(total_coins / 2)
        print(f"Game over! You've collected {total_coins} coins.")
        break

    # if field[new_pos[0]][new_pos[1]] > 0:
    total_coins += int(field[new_pos[0]][new_pos[1]])

    if total_coins >= 100:
        print(f"You won! You've collected {total_coins} coins.")
        break

path.append(player_pos)  # record path of the player
print("Your path:")
for point in range(len(path)):
    print(path[point])




