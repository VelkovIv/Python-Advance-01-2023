def get_magic_triangle(level):
    magic_triangle = []

    for index in range(level):
        if index == 0:
            magic_triangle.append([1])
            continue
        if index == 1:
            magic_triangle.append([1, 1])
            continue
        current_row = []

        for element in range(index + 1):
            if element == 0:
                current_row.append(1)
                continue
            if element == index:
                current_row.append(1)
                continue

            current_element = magic_triangle[index - 1][element - 1] + magic_triangle[index - 1][element]
            current_row.append(current_element)
        magic_triangle.append(current_row)

    return magic_triangle


num = int(input())
print(get_magic_triangle(num))
