def eat_cookie(santa_pos, presents_, nice_kids_with_present_):
    for direction in directions:
        new_row = santa_pos[0] + directions[direction][0]
        new_col = santa_pos[1] + directions[direction][1]

        if 0 <= new_row < size and 0 <= new_col < size:

            if neighborhood[new_row][new_col] != '-':
                if neighborhood[new_row][new_col] == 'V':
                    nice_kids_with_present_ += 1

                presents_ -= 1
                neighborhood[new_row][new_col] = '-'

        if presents_ == 0:
            break

    return presents_, nice_kids_with_present_


presents = int(input())
size = int(input())
neighborhood = []
santa_position = []
total_nice_kids = 0
nice_kids_with_present = 0

directions = {
    'up': (-1, 0),
    'down': (1, 0),
    'left': (0, -1),
    'right': (0, 1)
}

for row in range(size):
    neighborhood.append(input().split())

    if 'S' in neighborhood[row]:
        santa_position = [row, neighborhood[row].index('S')]
        neighborhood[row][santa_position[1]] = '-'

    if 'V' in neighborhood[row]:
        total_nice_kids += neighborhood[row].count('V')

command = input()

while command != 'Christmas morning':

    row = santa_position[0] + directions[command][0]
    col = santa_position[1] + directions[command][1]

    if 0 <= row < size and 0 <= col < size:
        position = neighborhood[row][col]
        neighborhood[row][col] = '-'
        santa_position = [row, col]

        if position == 'V':
            nice_kids_with_present += 1
            presents -= 1

        elif position == 'C':
            presents, nice_kids_with_present = eat_cookie(santa_position, presents, nice_kids_with_present)

    if presents == 0 or total_nice_kids == nice_kids_with_present:
        break

    command = input()

neighborhood[santa_position[0]][santa_position[1]] = 'S'

if not presents and total_nice_kids > nice_kids_with_present:
    print('Santa ran out of presents!')

[print(*row) for row in neighborhood]


if total_nice_kids == nice_kids_with_present:
    print(f'Good job, Santa! {total_nice_kids} happy nice kid/s.')
else:
    print(f'No presents for {total_nice_kids - nice_kids_with_present} nice kid/s.')