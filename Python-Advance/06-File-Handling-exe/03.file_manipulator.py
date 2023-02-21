import os

while True:
    command, *data = input().split("-")

    if command == "End":
        break

    if command == "Create":
        file = open(f"files/{data[0]}", 'w')
        file.close()

    elif command == "Add":
        with open(f"files/{data[0]}", 'a') as file:
            file.write(f"{data[1]}\n")

    elif command == "Replace":
        try:
            with open(f"files/{data[0]}", 'r') as file:
                text = file.readlines()
            for i in range(len(text)):
                text[i] = text[i].replace(data[1], data[2])

            file = open(f"files/{data[0]}", 'w')
            file.writelines(text)
            file.close()

        except FileNotFoundError:
            print("An error occurred")

    elif command == "Delete":
        try:
            os.remove(f"files/{data[0]}")

        except FileNotFoundError:
            print("An error occurred")
