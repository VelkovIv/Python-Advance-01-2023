
try:
    file = open('numbers.txt', 'r')
    result = 0

    for line in file:
        result += int(line)

    print(result)

    file.close()

except FileNotFoundError as error:
    print(error)