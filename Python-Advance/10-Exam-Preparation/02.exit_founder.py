players_names = input().split(', ')
# create a deque of players and status if hit the wall
players = [[players_names[0], False], [players_names[1], False]]

maze_size = 6
maze_board = []
current_position = [0, 0]
current_player = ''

for row in range(maze_size):
    maze_board.append(list(input().split()))

while True:
    coordinates = input()
    current_position[0] = int(coordinates[1])
    current_position[1] = int(coordinates[4])
    if players[0][1]:
        players[0][1] = False
        players[0], players[1] = players[1], players[0]
        continue
    current_player = players[0][0]

    if maze_board[current_position[0]][current_position[1]] == 'E':
        print(f"{current_player} found the Exit and wins the game!")
        break

    elif maze_board[current_position[0]][current_position[1]] == 'T':
        print(f"{current_player} is out of the game! The winner is {players[1][0]}.")
        break

    elif maze_board[current_position[0]][current_position[1]] == 'W':
        print(f"{current_player} hits a wall and needs to rest.")
        players[0][1] = True

    players[0], players[1] = players[1], players[0]
