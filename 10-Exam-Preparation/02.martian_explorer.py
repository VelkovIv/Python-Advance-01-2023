size = 6
field = []
water = 0
metal = 0
concrete = 0
rover_pos = []
suitable_for_colony = False

moves = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

for row in range(size):
    field.append(input().split())

    if "E" in field[row]:
        rover_pos = [row, field[row].index("E")]
        field[row][rover_pos[1]] = "-"

commands = input().split(', ')

while commands:
    command = commands.pop(0)
    rover_pos[0] += moves[command][0]
    rover_pos[1] += moves[command][1]

    # check the row if out of the field return to the other site
    if rover_pos[0] < 0:
        rover_pos[0] = size - 1
    elif rover_pos[0] > size - 1:
        rover_pos[0] = 0

    # check the column if out of the field return to the other site
    if rover_pos[1] < 0:
        rover_pos[1] = size -1
    elif rover_pos[1] > size - 1:
        rover_pos[1] = 0

    # main logic
    if field[rover_pos[0]][rover_pos[1]] == "W":
        print(f"Water deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        water += 1
    elif field[rover_pos[0]][rover_pos[1]] == "M":
        print(f"Metal deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        metal += 1
    elif field[rover_pos[0]][rover_pos[1]] == "C":
        print(f"Concrete deposit found at ({rover_pos[0]}, {rover_pos[1]})")
        concrete += 1
    elif field[rover_pos[0]][rover_pos[1]] == "R":
        print(f"Rover got broken at ({rover_pos[0]}, {rover_pos[1]})")
        break


if water >= 1 and metal >= 1 and concrete >= 1:
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")
