def rectangle(length, width):
    def area(l, w):
        return l * w

    def perimeter(l, w):
        return 2 * (l + w)

    if type(length) != int or type(width) != int:
        return "Enter valid values!"

    return f'''Rectangle area: {area(length, width)}
Rectangle perimeter: {perimeter(length, width)}'''


print(rectangle(2, 10))
print(rectangle('2', 10))