size = int(input())
bombs = int(input())
bombs_list = []
game_board = []
directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
    "up_left": (-1, -1),
    "up_right": (1, -1),
    "down_left": (-1, 1),
    "down_right": (1, 1),
}

# collecting bombs location
for _ in range(bombs):
    current_bomb = input()

    bombs_list.append([int(current_bomb[1:2]), int(current_bomb[4:5])])

# creating game board and placing the bombs
for i in range(size):
    game_board.append([0] * size)

for bomb in range(len(bombs_list)):
    row, col = bombs_list[bomb]
    game_board[row][col] = "*"

# mark the field around the bombs
for row in range(size):
    for col in range(size):
        bombs_counter = 0
        if game_board[row][col] == "*":
            continue
        for direction in directions:
            new_row = row + directions[direction][0]
            new_col = col + directions[direction][1]
            if 0 <= new_row < size and 0 <= new_col < size:
                if game_board[new_row][new_col] == "*":
                    bombs_counter += 1
        game_board[row][col] = bombs_counter

for row in range(size):
    print(" ".join(map(str, game_board[row])))
