from collections import deque

bees = deque(map(int, input().split()))
nectars = deque(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

operations = {
    '+': lambda a, b: a + b,
    '-': lambda a, b: a - b,
    '*': lambda a, b: a * b,
    '/': lambda a, b: a / b
}

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee > nectar:
        bees.appendleft(bee)
    elif bee <= nectar:
        next_symbol = symbols.popleft()
        total_honey += abs(operations[next_symbol](bee, nectar))

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectars:
    print(f'Nectar left: {", ".join(str(x) for x in nectars)}')
