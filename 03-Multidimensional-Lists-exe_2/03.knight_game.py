board_size = int(input())
board = [input() for _ in range(board_size)]

moves = (
    (-2, -1),
    (-2, 1),
    (-1, -2),
    (1, -2),
    (2, -1),
    (2, 1),
    (1, 2),
    (-1, 2),
)

remove_knight_count = 0

while True:
    knight_with_max_attack = [0, 0, 0]

    for row in range(board_size):
        for col in range(board_size):

            if board[row][col] == "K":
                attack = 0

                for move in moves:
                    new_row = row + move[0]
                    new_col = col + move[1]

                    if 0 <= new_row < board_size and 0 <= new_col < board_size:
                        if board[new_row][new_col] == "K":
                            attack += 1
                if attack > knight_with_max_attack[0]:
                    knight_with_max_attack[0] = attack
                    knight_with_max_attack[1] = row
                    knight_with_max_attack[2] = col

    if knight_with_max_attack[0] != 0:
        r, c = knight_with_max_attack[1], knight_with_max_attack[2]
        board[r] = board[r][:c] + "0" + board[r][c + 1:]
        remove_knight_count += 1
    else:
        break

print(remove_knight_count)
