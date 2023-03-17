def reverse_text(text):
    for el in reversed(text):
        yield el


for char in reverse_text("step"):
    print(char, end='')
