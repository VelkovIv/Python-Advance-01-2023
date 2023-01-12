from collections import deque

petrol_pumps = deque([[int(x) for x in input().split(" ")] for n in range(int(input()))])

index = 0
petrol_pumps_copy = petrol_pumps.copy()
tank_of_fuel = 0

while petrol_pumps_copy:
    petrol, distance = petrol_pumps_copy.popleft()

    tank_of_fuel += petrol

    if tank_of_fuel - distance < 0:
        petrol_pumps.rotate(-1)
        petrol_pumps_copy = petrol_pumps.copy()
        index += 1
        tank_of_fuel = 0

    else:
        tank_of_fuel -= distance


print(index)
