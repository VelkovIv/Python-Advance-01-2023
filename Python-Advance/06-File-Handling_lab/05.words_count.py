import re

with open('words.txt', 'r') as file:
    words = {}
    keys = []

    for line in file:
        keys = line.split()
        for key in keys:
            if key.lower() not in words.keys():
                words[key.lower()] = 0

with open('input.txt', 'r') as file:
    for line in file:
        for word in line.split():
            curr_word = re.findall(r'\w+', word)[0]
            if curr_word.lower() in words.keys():
                words[curr_word.lower()] += 1

for key, value in sorted(words.items(), key= lambda item: -item[1]):
    print(f'{key} - {value}')
