chemical_elements = set()

for _ in range(int(input())):
    for el in input().split():
        chemical_elements.add(el)

print(*chemical_elements, sep="\n")