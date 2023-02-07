from pyfiglet import figlet_format


def print_text(text):
    text = figlet_format(text, font='3-d')
    print(text)


print_text('Hello World')
