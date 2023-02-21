from collections import deque

green_light_duration = int(input())
free_window_duration = int(input())
cars = deque()

car_passed = 0
command = input()
character_hit = ''

while command != "END":

    if command == 'green':
        green_light = green_light_duration
        cars_left = cars.copy()

        if len(cars_left) > 0:

            while cars and green_light > 0:

                curr_car = cars.popleft()

                if green_light - len(curr_car) > 0:
                    green_light -= len(curr_car)
                    car_passed += 1

                elif green_light + free_window_duration - len(curr_car) >= 0:
                    green_light = 0
                    car_passed += 1

                elif green_light + free_window_duration - len(curr_car) < 0:
                    slice_ch = green_light + free_window_duration
                    character_hit = curr_car[slice_ch:slice_ch + 1]
                    print("A crash happened!")
                    print(f'{curr_car} was hit at {character_hit}.')
                    break

    else:
        cars.append(command)
    if character_hit:
        break
    command = input()

else:
    print("Everyone is safe.")
    print(f"{car_passed} total cars passed the crossroads.")