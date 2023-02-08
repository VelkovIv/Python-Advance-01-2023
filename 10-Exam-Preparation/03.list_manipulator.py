def list_manipulator(numbers, *data):
    result = []
    nums = numbers
    commands = [x for x in data]

    if commands[0] == 'add':
        commands.pop(0)

        if commands[0] == 'beginning':
            commands.pop(0)
            commands.extend(nums)
            result = commands

        elif commands[0] == 'end':
            commands.pop(0)
            nums.extend(commands)
            result = nums

    elif commands[0] == 'remove':
        if len(commands) == 2:
            if commands[1] == 'beginning':
                nums.pop(0)

            elif commands[1] == 'end':
                nums.pop()

        elif commands[1] == 'beginning':
            commands.pop(0)
            commands.pop(0)
            for _ in range(commands[0]):
                nums.pop(0)
        elif commands[1] == 'end':
            commands.pop(0)
            commands.pop(0)
            for _ in range(commands[0]):
                nums.pop()
        result = nums

    return result


print(list_manipulator([1, 2, 3], "remove", "end"))
print(list_manipulator([1, 2, 3], "remove", "beginning"))
print(list_manipulator([1, 2, 3], "add", "beginning", 20))
print(list_manipulator([1, 2, 3], "add", "end", 30))
print(list_manipulator([1, 2, 3], "remove", "end", 2))
print(list_manipulator([1, 2, 3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1, 2, 3], "add", "end", 30, 40, 50))
