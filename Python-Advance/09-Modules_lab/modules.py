import operator as op


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


def calculation(first_num, operator, second_num):
    operations = {"+": op.add, "-": op.sub, "*": op.mul, "/": op.truediv, "^": op.pow}

    return operations[operator](first_num, second_num)


sequence = []


def create_fibonacci_sequence(num):
    sequence.clear()
    sequence.append(0)
    sequence.append(1)

    for _ in range(num - 2):
        sequence.append(sequence[-2] + sequence[-1])

    return f'{" ".join(map(str, sequence))}'


def locate_number(num):
    if num in sequence:
        index = sequence.index(num)
        return f'The number - {num} is at index {index}'
    else:
        return f'The number {num} is not in the sequence'