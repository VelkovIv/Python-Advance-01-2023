from collections import deque

textiles = deque([int(el) for el in input().split()])
medicaments = [int(el) for el in input().split()]

created_items = {
    "Patch": 0,
    "Bandage": 0,
    "MedKit": 0,
}

patch_value = 30
bandage_value = 40
medkit_value = 100
current_combination = 0

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medeciament = medicaments.pop()
    current_combination = current_textile + current_medeciament

    if current_combination > medkit_value:
        created_items["MedKit"] += 1
        last_medicament = medicaments.pop() + (current_combination - medkit_value)
        medicaments.append(last_medicament)

    elif current_combination == medkit_value:
        created_items["MedKit"] += 1
    elif current_combination == bandage_value:
        created_items["Bandage"] += 1
    elif current_combination == patch_value:
        created_items["Patch"] += 1

    else:
        medicaments.append(current_medeciament + 10)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

if not textiles and medicaments:
    print("Textiles are empty.")

if not medicaments and textiles:
    print("Medicaments are empty.")

for k, v in sorted(created_items.items(), key=lambda x: (-x[1], x[0])):
    if v > 0:
        print(f"{k} - {v}")

if medicaments:
    print(f"Medicaments left: {', '.join([str(medicaments[i]) for i in range(len(medicaments) - 1, -1, -1)])}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")
