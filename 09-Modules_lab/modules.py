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
