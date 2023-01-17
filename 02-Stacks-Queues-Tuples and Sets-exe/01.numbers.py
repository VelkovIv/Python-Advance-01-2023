first_seq = set(int(x) for x in input().split())
second_seq = set(int(x) for x in input().split())

operations = {
    "Add First": lambda x: [first_seq.add(el) for el in x],
    "Add Second": lambda x: [second_seq.add(el) for el in x],
    "Remove First": lambda x: [first_seq.discard(el) for el in x],
    "Remove Second": lambda x: [second_seq.discard(el) for el in x],
    "Check Subset": lambda: print(True) if first_seq.issubset(second_seq) or second_seq.issubset(first_seq) \
        else print(False)
}

for cmd in range(int(input())):
    first_command, *data = input().split()
    current_command = first_command + ' ' + data.pop(0)

    if data:
        operations[current_command](int(x) for x in data)
    else:
        operations[current_command]()

print(*sorted(first_seq), sep=", ")
print(*sorted(second_seq), sep=", ")


