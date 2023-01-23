rows, cols = map(int, input().split())

for row in range(rows):
    for col in range(cols):
        print(f'{chr(row + 97)}{chr(col + row + 97)}{chr(row + 97)}', end=' ')
    print()
