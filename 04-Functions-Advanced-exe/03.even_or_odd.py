def even_odd(*args):
    command = args[-1]
    results = []

    for el in args[:-1]:
        if el % 2 == 0 and command == 'even':
            results.append(el)
        elif el % 2 != 0 and command == 'odd':
            results.append(el)
    return results


print(even_odd(1, 2, 3, 4, 5, 6, "even"))
print(even_odd(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "odd"))