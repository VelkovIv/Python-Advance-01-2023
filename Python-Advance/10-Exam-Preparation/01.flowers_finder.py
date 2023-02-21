from collections import deque

vowels = deque(list(input().split()))
consonants = list(input().split())
flower_found = False
flowers_to_check = {'rose': 'rose', 'tulip': 'tulip', 'lotus': 'lotus', 'daffodil': 'daffodil'}
f_counter = 0

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower, name in flowers_to_check.items():
        if current_vowel in flower:
            flowers_to_check[flower] = flowers_to_check[flower].replace(current_vowel, '')

        if current_consonant in flower:
            flowers_to_check[flower] = flowers_to_check[flower].replace(current_consonant, '')

    for flower, name in flowers_to_check.items():
        if len(name) == 0:
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

