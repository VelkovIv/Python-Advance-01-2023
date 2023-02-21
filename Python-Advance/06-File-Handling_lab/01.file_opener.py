try:
    file = open('text.txt', 'r')

except FileNotFoundError as error:
    print('File not found')

else:
    print('File found')