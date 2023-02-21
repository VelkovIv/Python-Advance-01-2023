def func_executor(*func_arguments):
    results = []

    for func, args in func_arguments:
        results.append(f"{func.__name__} - {func(*args)}")

    return '\n'.join(results)


def sum_numbers(num1, num2):
    return num1 + num2


def multiply_numbers(num1, num2):
    return num1 * num2


print(func_executor(
    (sum_numbers, (1, 2)),
    (multiply_numbers, (2, 4))
))
