def rhombus(size: int):
    for i in range(1, size + 1):
        spaces = ' ' * (size - i)
        stars = '* ' * i
        print(spaces + stars)

    for i in range(size - 1, 0, -1):
        spaces = ' ' * (size - i)
        stars = '* ' * i
        print(spaces + stars)


number = int(input())
rhombus(number)
