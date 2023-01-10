from _collections import deque

water_quantity = int(input())
queue_for_water = deque()

current_command = input()
while current_command != "Start":
    queue_for_water.append(current_command)
    current_command = input()
while current_command != "End":

    if current_command.isdigit():

        if int(current_command) <= water_quantity:
            water_quantity -= int(current_command)
            print(f"{queue_for_water.popleft()} got water")
        else:
            print(f"{queue_for_water.popleft()} must wait")

    elif current_command.startswith("refill"):
        water = current_command.split(" ")
        water_quantity += int(water[1])

    current_command = input()
print(f"{water_quantity} liters left")