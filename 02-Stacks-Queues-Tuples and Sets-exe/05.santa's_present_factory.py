from collections import deque

crafting_materials = deque(map(int, input().split()))
magic_level = deque(map(int, input().split()))

toys = {
    150: "Doll",
    250: "Wooden train",
    300: "Teddy bear",
    400: "Bicycle"
}

crafted_toys = {}

while crafting_materials and magic_level:

    if crafting_materials[-1] == 0 and magic_level[0] == 0:
        crafting_materials.pop()
        magic_level.popleft()
        continue
    elif crafting_materials[-1] == 0:
        crafting_materials.pop()
        continue
    elif magic_level[0] == 0:
        magic_level.popleft()
        continue

    current_material = crafting_materials.pop()
    current_magic = magic_level.popleft()

    product = current_material * current_magic

    if product in toys.keys():
        if toys[product] not in crafted_toys.keys():
            crafted_toys[toys[product]] = 0
        crafted_toys[toys[product]] += 1

    elif product < 0:
       new_material = abs(current_material + current_magic)
       crafting_materials.append(new_material)
    elif product > 0:
        crafting_materials.append(current_material + 15)


if {'Bicycle', 'Teddy bear'}.issubset(set(crafted_toys.keys())) or\
        {'Wooden train', 'Doll'}.issubset(set(crafted_toys.keys())):
    print('The presents are crafted! Merry Christmas!')
else:
    print('No presents this Christmas!')

if crafting_materials:
    crafting_materials.reverse()
    print(f'Materials left: {", ".join(str(x) for x in  crafting_materials)}')

if magic_level:
    print(f'Magic left: {", ".join(map(str, magic_level))}')

for k, v in sorted(crafted_toys.items(), key=lambda x: x[0]):
    print(f'{k}: {v}')