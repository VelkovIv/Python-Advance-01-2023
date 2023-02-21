from functools import reduce


def operate(operator, *args):
    def multiply(*nums):
        return reduce(lambda x, y: x * y, nums)

    def division(*nums):
        if 0 in nums:
            return 0
        return reduce(lambda x, y: x / y, nums)

    def sums(*nums):
        return reduce(lambda x, y: x + y, nums)

    def subtract(*nums):
        return reduce(lambda x, y: x - y, nums)

    if operator == '+':
        return sums(*args)
    elif operator == '-':
        return subtract(*args)
    elif operator == '*':
        return multiply(*args)
    elif operator == '/':
        return division(*args)
    else:
        return 0


print(operate("/", 1, 2, -3, 4))
# print(operate("*", 3, 4, 5, 6, 7))
