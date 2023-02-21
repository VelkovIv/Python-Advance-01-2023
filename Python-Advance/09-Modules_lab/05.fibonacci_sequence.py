from modules import create_fibonacci_sequence, locate_number

command, *data = input().split()

while command != 'Stop':
    if command == 'Create':
        number = int(data[1])
        print(create_fibonacci_sequence(number))

    elif command == 'Locate':
        number = int(data[0])
        print(locate_number(number))

    command, *data = input().split()
