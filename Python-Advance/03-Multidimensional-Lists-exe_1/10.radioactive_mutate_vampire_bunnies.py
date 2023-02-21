def bunny_spread_func(matrix, bunny_positions):
    bunny_positions_ = bunny_positions
    for i in range(len(bunny_positions)):
        for move in moves:
            new_row = bunny_positions[i][0] + moves[move][0]
            new_col = bunny_positions[i][1] + moves[move][1]
            if 0 <= new_row < len(matrix) and 0 <= new_col < len(matrix[0]):
                matrix[new_row][new_col] = "B"
            bunny_positions_.append([new_row, new_col])

    return matrix, bunny_positions_


rows, cols = input().split()
rows = int(rows)
cols = int(cols)

lair = []
bunny_pos = []
player_pos = []
dead = False
won = False

moves = {
    "U": (-1, 0),
    "D": (1, 0),
    "L": (0, -1),
    "R": (0, 1)
}

for row in range(rows):

    lair.append(list(input()))

    if "B" in lair[row]:
        bunny_pos.append([row, lair[row].index("B")])

    if "P" in lair[row]:
        player_pos = [row, lair[row].index("P")]
        lair[row][player_pos[1]] = "."

commands = [x for x in input()]

while True:
    # if commands:
    new_move = commands.pop(0)
    new_player_pos = [
        player_pos[0] + moves[new_move][0],
        player_pos[1] + moves[new_move][1]
    ]

    lair, bunny_pos = bunny_spread_func(lair, bunny_pos)

    if not (0 <= new_player_pos[0] < rows and 0 <= new_player_pos[1] < cols):
        won = True
        break

    if lair[new_player_pos[0]][new_player_pos[1]] == 'B':
        dead = True
        break

    player_pos = new_player_pos

for row in lair:
    print(''.join(row))

if dead:
    print(f'dead: {new_player_pos[0]} {new_player_pos[1]}')

if won:
    print(f'won: {player_pos[0]} {player_pos[1]}')
