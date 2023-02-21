from math import log

number = int(input('Enter a number: '))
base = input('Enter a base: ')

if base == 'natural':
    result = log(number)
else:
    result = log(number, int(base))

print(f'{result:.2f}')