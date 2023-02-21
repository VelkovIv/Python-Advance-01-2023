rows, cols = map(int, input().split(', '))

commands = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

santa_workshop = []
santa_pos = []
decorations = 0
gifts = 0
cookies = 0
decorations_taken = 0
gifts_taken = 0
cookies_taken = 0
all_collected = False

for row in range(rows):
    santa_workshop.append(input().split())

    if "D" in santa_workshop[row]:
        decorations += santa_workshop[row].count("D")

    if "G" in santa_workshop[row]:
        gifts += santa_workshop[row].count("G")

    if "C" in santa_workshop[row]:
        cookies += santa_workshop[row].count("C")

    if "Y" in santa_workshop[row]:
        santa_pos = [row, santa_workshop[row].index("Y")]
        santa_workshop[row][santa_pos[1]] = "x"

current_command = input().split('-')

while current_command[0] != "End":
    move, steps = current_command[0], int(current_command[1])

    for step in range(steps):
        new_pos = [santa_pos[0] + commands[move][0], santa_pos[1] + commands[move][1]]
        if abs(new_pos[0]) > rows -1:
            new_pos[0] = 0
        if abs(new_pos[1]) > cols - 1:
            new_pos[1] = 0

        if santa_workshop[new_pos[0]][new_pos[1]] == "D":
            decorations -= 1
            decorations_taken += 1
        elif santa_workshop[new_pos[0]][new_pos[1]] == "G":
            gifts -= 1
            gifts_taken += 1
        elif santa_workshop[new_pos[0]][new_pos[1]] == "C":
            cookies -= 1
            cookies_taken += 1

        santa_workshop[santa_pos[0]][santa_pos[1]] = "x"
        santa_pos = new_pos

        if decorations == 0 and gifts == 0 and cookies == 0:
            all_collected = True
            break

    if all_collected:
        break
    current_command = input().split('-')

santa_workshop[santa_pos[0]][santa_pos[1]] = "Y"

if all_collected:
    print("Merry Christmas!")

print("You've collected:")
print(f"- {decorations_taken} Christmas decorations")
print(f"- {gifts_taken} Gifts")
print(f"- {cookies_taken} Cookies")

for row in range(rows):
    print(" ".join(santa_workshop[row]))
