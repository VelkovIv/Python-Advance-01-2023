size = 8
chess_board = []
captures_white = {
    "0": [-1, -1],
    "1": [-1, 1],
    "2": [-1, 0]
}

captures_black = {
    "0": [1, -1],
    "1": [1, 1],
    "2": [1, 0]
}
columns = ["a", "b", "c", "d", "e", "f", "g", "h"]
black_pos = []
white_pos = []

# make the board
for row in range(size):
    chess_board.append(input().split())

    if 'b' in chess_board[row]:
        black_pos = [row, int(chess_board[row].index('b'))]

    if 'w' in chess_board[row]:
        white_pos = [row, int(chess_board[row].index('w'))]

# main logic
while True:
    # check possibilities of promoting a pawn
    if abs(white_pos[1] - black_pos[1]) > 1:
        if white_pos[0] < size - black_pos[0]:
            square = columns[white_pos[1]] + str(8)
            print(f"Game over! White pawn is promoted to a queen at {square}.")
            break
        else:
            square = columns[black_pos[1]] + str(1)
            print(f"Game over! Black pawn is promoted to a queen at {square}.")
            break

    # white possible moves
    left = [white_pos[0] + captures_white['0'][0], white_pos[1] + captures_white['0'][1]]
    right = [white_pos[0] + captures_white['1'][0], white_pos[1] + captures_white['1'][1]]
    forward = [white_pos[0] + captures_white['2'][0], white_pos[1] + captures_white['2'][1]]
    # check for captures - left and right diagonal
    if chess_board[left[0]][left[1]] == 'b':
        square = columns[left[1]] + str(size - left[0])
        print(f"Game over! White win, capture on {square}.")
        break
    elif chess_board[right[0]][right[1]] == 'b':
        square = columns[right[1]] + str(size - right[0])
        print(f"Game over! White win, capture on {square}.")
        break
    # move forward
    else:
        chess_board[white_pos[0]][white_pos[1]] = '-'
        chess_board[forward[0]][forward[1]] = 'w'
        white_pos = forward

    # black possible moves
    left = [black_pos[0] + captures_black['0'][0], black_pos[1] + captures_black['0'][1]]
    right = [black_pos[0] + captures_black['1'][0], black_pos[1] + captures_black['1'][1]]
    forward = [black_pos[0] + captures_black['2'][0], black_pos[1] + captures_black['2'][1]]
    # check for captures - left and right diagonal
    if chess_board[left[0]][left[1]] == 'w':
        square = columns[left[1]] + str(left[0] + 1)
        print(f"Game over! Black win, capture on {square}.")
        break
    elif chess_board[right[0]][right[1]] == 'w':
        square = columns[right[1]] + str(right[0] + 1)
        print(f"Game over! Black win, capture on {square}.")
        break
    # move forward
    else:
        chess_board[black_pos[0]][black_pos[1]] = '-'
        chess_board[forward[0]][forward[1]] = 'b'
        black_pos = forward
