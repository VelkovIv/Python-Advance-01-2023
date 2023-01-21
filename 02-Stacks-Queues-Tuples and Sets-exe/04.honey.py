from collections import deque


def honey_calc(curr_bee, cur_nectar, curr_symbol):
    if curr_symbol == '*':
        return abs(curr_bee * cur_nectar)
    elif curr_symbol == '/':
        return abs(curr_bee / cur_nectar)
    elif curr_symbol == '+':
        return abs(curr_bee + cur_nectar)
    elif curr_symbol == '-':
        return abs(curr_bee - cur_nectar)


bees = deque(map(int, input().split()))
nectars = deque(map(int, input().split()))
symbols = deque(input().split())

total_honey = 0

while bees and nectars:
    bee = bees.popleft()
    nectar = nectars.pop()

    if bee > nectar:
        bees.appendleft(bee)
    elif bee <= nectar:
        next_symbol = symbols.popleft()
        current_honey = honey_calc(bee, nectar, next_symbol)
        total_honey += current_honey

print(f'Total honey made: {total_honey}')
if bees:
    print(f'Bees left: {", ".join(str(x) for x in bees)}')
if nectars:
    print(f'Nectar left: {", ".join(str(x) for x in  nectars)}')
