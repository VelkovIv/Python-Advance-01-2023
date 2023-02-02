from string import punctuation

with open("files/text.txt", 'r') as file:
    text = file.readlines()

result = ''
with open("files/output.txt", 'w') as file:

    for i in range(len(text)):
        letters = 0
        symbols = 0
        for symbol in text[i]:
            if symbol.isalpha():
                letters += 1

            elif symbol in punctuation:
                symbols += 1

        result += f"Line {i + 1}: {text[i][:-1]} ({letters})({symbols})\n"
    file.write(result)
