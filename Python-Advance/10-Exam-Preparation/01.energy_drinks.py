from collections import deque

milligrams_of_caffeine = deque(map(int, input().split(', ')))
energy_drinks = deque(map(int, input().split(', ')))

MAX_CAFFEINE_FOE_NIGHT = 300
total_caffeine = 0

while milligrams_of_caffeine and energy_drinks:
    current_caffeine, current_drink = milligrams_of_caffeine.pop(), energy_drinks.popleft()
    caffeine = current_caffeine * current_drink

    if (total_caffeine + caffeine) <= MAX_CAFFEINE_FOE_NIGHT:
        total_caffeine += caffeine
    else:
        if total_caffeine - 30 < 0:
            total_caffeine = 0
        else:
            total_caffeine -= 30
        energy_drinks.append(current_drink)

if energy_drinks:
    print(f'Drinks left: {", ".join(map(str, energy_drinks))}')
else:
    print("At least Stamat wasn't exceeding the maximum caffeine.")
print(f'Stamat is going to sleep with {total_caffeine} mg caffeine.')