def repeated_text(text, num):
    return text * num


try:
    word = input("Enter a word: ")
    repeat = int(input("How many times do you want to repeat the word? "))
    print(repeated_text(word, repeat))

except ValueError:
    print("Variable times must be an integer")
