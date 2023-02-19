rows, cols = input().split()
rows = int(rows)
cols = int(cols)

start_pos = []
playground = []
touched_opponents = 0
moves = 0
opponents = 0

move = {
    'left': (0, -1),
    'right': (0, 1),
    'up': (-1, 0),
    'down': (1, 0)
}

for row in range(rows):
    playground.append(list(input().split()))

    if "B" in playground[row]:
        start_pos = [row, playground[row].index("B")]
        playground[row][start_pos[1]] = "-"

    if "P" in playground[row]:
        opponents += playground[row].count("P")

command = input()
while command != "Finish":
    new_pos = [start_pos[0] + move[command][0], start_pos[1] + move[command][1]]

    if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols:
        if playground[new_pos[0]][new_pos[1]] == "P":
            touched_opponents += 1
            playground[new_pos[0]][new_pos[1]] = "-"
            moves += 1
            start_pos = new_pos

        elif playground[new_pos[0]][new_pos[1]] == "O":
            pass

        elif playground[new_pos[0]][new_pos[1]] == "-":
            moves += 1
            start_pos = new_pos

    if touched_opponents == 3:
        break

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_opponents} Moves made: {moves}")
