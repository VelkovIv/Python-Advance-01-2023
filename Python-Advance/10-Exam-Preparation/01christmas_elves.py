elfs_energy = list(map(int, input().split()))
number_of_materials = list(map(int, input().split()))

total_elfs_energy = 0
total_toys = 0
counter = 1
cookie = 1
no_more_energy = False

while elfs_energy and number_of_materials:
    current_elfs_energy = elfs_energy.pop(0)
    while current_elfs_energy < 5:
        if elfs_energy:
            current_elfs_energy = elfs_energy.pop(0)
        else:
            no_more_energy = True
            break
    if no_more_energy:
        break

    current_materials = number_of_materials.pop()

    if counter % 3 == 0:

        if current_elfs_energy >= current_materials * 2:
            current_elfs_energy -= current_materials * 2
            total_elfs_energy += current_materials * 2
            if counter % 5 == 0:
                elfs_energy.append(current_elfs_energy)
            else:
                total_toys += 2
                elfs_energy.append(current_elfs_energy + cookie)
        else:
            current_elfs_energy *= 2
            elfs_energy.append(current_elfs_energy)
            number_of_materials.append(current_materials)

    elif counter % 5 == 0:
        if current_elfs_energy >= current_materials:
            current_elfs_energy -= current_materials
            total_elfs_energy += current_materials
            elfs_energy.append(current_elfs_energy)
        else:
            current_elfs_energy *= 2
            elfs_energy.append(current_elfs_energy)
            number_of_materials.append(current_materials)

    elif current_elfs_energy >= current_materials:
        current_elfs_energy -= current_materials
        total_elfs_energy += current_materials
        total_toys += 1
        elfs_energy.append(current_elfs_energy + cookie)
    else:
        current_elfs_energy *= 2
        elfs_energy.append(current_elfs_energy)
        number_of_materials.append(current_materials)

    counter += 1

print(f"Toys: {total_toys}")
print(f"Energy: {total_elfs_energy}")
if elfs_energy:
    print(f"Elves left: {', '.join(map(str, elfs_energy))}")

if number_of_materials:
    print(f"Boxes left: {', '.join(map(str, number_of_materials))}")