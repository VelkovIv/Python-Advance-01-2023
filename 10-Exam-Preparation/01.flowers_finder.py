from collections import deque

vowels = deque(list(input().split()))
consonants = deque(list(input().split()))
flower_found = False
flowers_to_check = {'rose': [], 'tulip': [], 'lotus': [], 'daffodil': []}
f_counter = 0

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower, name in flowers_to_check.items():
        if current_vowel in flower and current_vowel not in name:
            flowers_to_check[flower].append(current_vowel)

        if current_consonant in flower:
            if current_consonant == 'f' and f_counter <= 2:
                flowers_to_check[flower].append(current_consonant)
                f_counter += 1
            elif current_consonant not in name:
                flowers_to_check[flower].append(current_consonant)

    for flower, name in flowers_to_check.items():
        if len(flower) == len(name):
            print(f"Word found: {flower}")
            flower_found = True
            break
    if flower_found:
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")

if consonants:
    print(f"Consonants left: {' '.join(consonants)}")

