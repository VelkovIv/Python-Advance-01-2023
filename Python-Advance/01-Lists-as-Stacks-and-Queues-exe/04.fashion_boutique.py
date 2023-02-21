box_with_clothes = input().split(" ")
rack_size = int(input())
rack_number = 0
current_rack = 0

while box_with_clothes:
    current_clothing = int(box_with_clothes.pop())

    if rack_number == 0:
        rack_number = 1

    if rack_size - current_rack >= current_clothing:
        current_rack += current_clothing

    else:
        current_rack = 0
        rack_number += 1
        current_rack += current_clothing

print(rack_number)
