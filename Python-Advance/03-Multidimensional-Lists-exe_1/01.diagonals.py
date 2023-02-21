data = [[int(el) for el in input().split(', ')] for _ in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for row in range(len(data)):
    primary_diagonal.append(data[row][row])

for row in range(len(data)):
    secondary_diagonal.append(data[row][(len(data) - 1) - row])

print(f'Primary diagonal: {", ".join(str(x) for x in primary_diagonal)}. Sum: {sum(primary_diagonal)}')
print(f'Secondary diagonal: {", ".join(str(x) for x in secondary_diagonal)}. Sum: {sum(secondary_diagonal)}')

