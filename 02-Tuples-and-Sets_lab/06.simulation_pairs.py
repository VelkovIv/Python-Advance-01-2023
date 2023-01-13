import time

numbers = list(map(int, input().split(' ')))
target_num = int(input())

start = time.time()

for f_num in range(len(numbers)):

    if numbers[f_num] != 'x':

        for s_num in range(f_num + 1, len(numbers)):

            if numbers[s_num] != 'x':

                if numbers[f_num] + numbers[s_num] == target_num:
                    print(f'{numbers[f_num]} + {numbers[s_num]} == {target_num}')

                    numbers[f_num], numbers[s_num] = 'x', 'x'

                    break
end = time.time()
print(f'Time execution: {end - start}')
