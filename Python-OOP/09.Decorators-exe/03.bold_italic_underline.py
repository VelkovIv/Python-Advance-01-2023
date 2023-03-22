def make_bold(func):
    def wreapper(*args):
        result = func(*args)
        return f'<b>{result}</b>'

    return wreapper

def make_italic(func):
    def wreapper(*args):
        result = func(*args)
        return f'<i>{result}</i>'

    return wreapper


def make_underline(func):
    def wreapper(*args):
        result = func(*args)
        return f'<u>{result}</u>'

    return wreapper

@make_bold
@make_italic
@make_underline
def greet(name):
    return f"Hello, {name}"


print(greet("Peter"))


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"


print(greet_all("Peter", "George"))
