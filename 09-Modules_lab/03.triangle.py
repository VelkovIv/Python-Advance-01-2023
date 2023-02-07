def print_triangle(num):
    result = ''
    for n in range(1, num + 1):
        for m in range(1, n + 1):
            result += f'{m} '
        result += '\n'

    for n in range(num - 1, 0, -1):
        for m in range(1, n + 1):
            result += f'{m} '
        result += '\n'

    return result


number = int(input('Enter a number: '))
print(print_triangle(number))
