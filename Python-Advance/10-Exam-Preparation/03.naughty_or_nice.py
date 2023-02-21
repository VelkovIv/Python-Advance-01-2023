def naughty_or_nice_list(kids, *commands, **naughty_or_nice):
    naughty_or_nice_dict = {
        "Nice": [],
        "Naughty": [],
        "Not found": []
    }
    result = ''

    for action in commands:
        num, key = action.split('-')
        num = int(num)
        kids_name = []
        for kid in kids:
            if num in kid:
                kids_name.append(kid)
        if len(kids_name) == 1:
            naughty_or_nice_dict[key].append(kids_name[0][1])
            kids.remove(kids_name[0])

    for name, key in naughty_or_nice.items():
        kids_name = []
        for kid in kids:
            if name in kid:
                kids_name.append(kid)
        if len(kids_name) == 1:
            naughty_or_nice_dict[key].append(kids_name[0][1])
            kids.remove(kids_name[0])

    for kid in kids:
        naughty_or_nice_dict["Not found"].append(kid[1])

    for kid_type, names in naughty_or_nice_dict.items():
        if len(names) > 0:
            result += f"{kid_type}: {', '.join(names)}\n"

    return result


print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))
print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))

print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))
