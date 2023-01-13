def print_func(cars_plates_nums):
    if cars_plates_nums:
        print(*cars_plates_nums, sep="\n")
    else:
        print('Parking Lot is Empty')


parking_data = [input() for _ in range(int(input()))]

cars_plates_data = set()
COMMAND_IN = "IN"
COMMAND_OUT = "OUT"

for num in range(len(parking_data)):
    command, plate = parking_data[num].split(', ')

    if command == COMMAND_IN:
        cars_plates_data.add(plate)

    elif command == COMMAND_OUT:
        cars_plates_data.remove(plate)

print_func(cars_plates_data)
