matrix = [[int(el) for el in input().split()] for _ in range(int(input()))]

primary_diagonal = []
secondary_diagonal = []

for row in range(len(matrix)):
    primary_diagonal.append(matrix[row][row])

for row in range(len(matrix)):
    secondary_diagonal.append(matrix[row][len(matrix) - row - 1])

diagonal_difference = abs(sum(primary_diagonal) - sum(secondary_diagonal))

print(diagonal_difference)