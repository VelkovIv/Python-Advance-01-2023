from collections import deque


def best_list_pureness(*input_data):
    element_sum = 0
    pureness = {}
    max_pureness = 0
    data, num = deque(input_data[0]), input_data[1]
    for rotation in range(num + 1):
        for i in range(len(data)):
            element_sum += i * data[i]

        if element_sum > max_pureness:
            max_pureness = element_sum
            rotation_value = rotation

        element_sum = 0
        data.rotate()

    return f"Best pureness {max_pureness} after {rotation_value} rotations"


test = ([4, 3, 2, 6], 4)
result = best_list_pureness(*test)
print(result)
test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
test = ([1, 2, 3, 4, 5], 10)
result = best_list_pureness(*test)
print(result)
test = ([1, 1, 1, 1, 1], 10)
result = best_list_pureness(*test)
print(result)
