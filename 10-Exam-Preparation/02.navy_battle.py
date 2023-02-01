size = int(input())
battlefield = []
submarine_pos = []
mine_hit = 0
cruisers_hit = 0

direction = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    battlefield.append(list(input()))

    if 'S' in battlefield[row]:
        submarine_pos = [row, battlefield[row].index('S')]
        battlefield[row][submarine_pos[1]] = '-'

while True:
    command = input()

    new_submarine_pos = [submarine_pos[0] + direction[command][0], submarine_pos[1] + direction[command][1]]

    if battlefield[new_submarine_pos[0]][new_submarine_pos[1]] == '*':
        mine_hit += 1
        battlefield[new_submarine_pos[0]][new_submarine_pos[1]] = '-'

    if mine_hit == 3:
        print(
            f'Mission failed, U-9 disappeared! Last known coordinates [{new_submarine_pos[0]}, {new_submarine_pos[1]}]!')
        break

    if battlefield[new_submarine_pos[0]][new_submarine_pos[1]] == 'C':
        cruisers_hit += 1
        battlefield[new_submarine_pos[0]][new_submarine_pos[1]] = '-'

    if cruisers_hit == 3:
        print('Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!')
        break

    submarine_pos = new_submarine_pos

battlefield[new_submarine_pos[0]][new_submarine_pos[1]] = 'S'

for row in range(size):
    print(''.join(battlefield[row]))