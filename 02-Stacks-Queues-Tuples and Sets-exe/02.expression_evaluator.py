from functools import reduce

expression = input().split()

operations = {
    "*": lambda x: reduce(lambda a, b: int(a) * int(b), expression[:x]),
    "/": lambda x: reduce(lambda a, b: int(int(a) / int(b)), expression[:x]),
    "+": lambda x: reduce(lambda a, b: int(a) + int(b), expression[:x]),
    "-": lambda x: reduce(lambda a, b: int(a) - int(b), expression[:x]),
}

idx = 0

while idx < len(expression):
    element = expression[idx]

    if element in "*/+-":
        result = operations[element](idx)
        expression = expression[idx+1:]
        expression.insert(0, result)
        idx = 0

    idx += 1

print(*expression)