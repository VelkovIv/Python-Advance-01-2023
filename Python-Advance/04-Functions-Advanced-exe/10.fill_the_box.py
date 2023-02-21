def fill_the_box(height, length,  width, *data):
    vol = height * length * width
    cubes = 0

    for num in range(len(data)):
        if data[num] == 'Finish':
            break
        cubes += data[num]
    space = vol - cubes
    if space > 0:
        return f'There is free space in the box. You could put {space} more cubes.'
    else:
        return f'No more free space! You have {abs(space)} more cubes.'


print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))
print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
print(fill_the_box(10, 10, 10, 40, "Finish", 2, 15, 30))