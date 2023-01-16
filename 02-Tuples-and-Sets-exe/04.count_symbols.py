text_character = {}

for ch in input():
    if ch not in text_character.keys():
        text_character[ch] = 0

    text_character[ch] += 1

for k, v in sorted(text_character.items()):
    print(f'{k}: {v} time/s')