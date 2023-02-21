def age_assignment(*names, **kwargs):
    result = ''

    for name in sorted(names):
        for key, value in kwargs.items():
            if key in name:
                result += f"{name} is {value} years old.\n"
    return result


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))
print(age_assignment("Peter", "George", G=26, P=19))
