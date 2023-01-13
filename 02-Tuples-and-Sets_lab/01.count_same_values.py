input_data = tuple(map(float, input().split(' ')))
repeated_numbers = {}

for num in input_data:
    if num not in repeated_numbers.keys():
        repeated_numbers[num] = 0

    repeated_numbers[num] += 1

for k, v in repeated_numbers.items():
    print(f"{k:.1f} - {v} times")

