size = int(input())

snake_territory = []

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

snake_pos = []
burrows_pos = []
food_numbers = 0
eaten_foot = 0

for row in range(size):
    snake_territory.append(list(input()))

    if "S" in snake_territory[row]:
        snake_pos = [row, snake_territory[row].index("S")]
        snake_territory[row][snake_pos[1]] = "."

    if "B" in snake_territory[row]:
        burrows_pos.append([row, snake_territory[row].index("B")])

    if "*" in snake_territory[row]:
        food_numbers += snake_territory[row].count("*")

while True:
    move = input()
    new_pos = [snake_pos[0] + moves[move][0], snake_pos[1] + moves[move][1]]

    if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size:
        if snake_territory[new_pos[0]][new_pos[1]] == "*":
            eaten_foot += 1
            snake_territory[new_pos[0]][new_pos[1]] = "."
        elif snake_territory[new_pos[0]][new_pos[1]] == "B":
            if new_pos == burrows_pos[0]:
                new_pos = burrows_pos[1]
            elif new_pos == burrows_pos[1]:
                new_pos = burrows_pos[0]
            snake_territory[burrows_pos[0][0]][burrows_pos[0][1]] = "."
            snake_territory[burrows_pos[1][0]][burrows_pos[1][1]] = "."
        else:
            snake_territory[new_pos[0]][new_pos[1]] = "."

    else:
        print("Game over!")
        break

    if eaten_foot == 10:
        print("You won! You fed the snake.")
        break

    snake_pos = new_pos

print(f"Food eaten: {eaten_foot}")
if 0 <= new_pos[0] < size and 0 <= new_pos[1] < size:
    snake_territory[new_pos[0]][new_pos[1]] = "S"

for row in snake_territory:
    print("".join(row))