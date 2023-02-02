symbols = ["-", ",", ".", "!", "?"]

with open("files/text.txt", "r") as file:
    text = file.readlines()

for i in range(0, len(text), 2):

    for symbol in symbols:
        text[i] = text[i].replace(symbol, "@")

    result = text[i].split()
    print(*result[::-1])