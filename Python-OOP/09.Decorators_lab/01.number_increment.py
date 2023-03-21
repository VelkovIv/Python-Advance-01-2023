def number_increment(numbers):
    def increase():
        num = [n + 1 for n in numbers]

        return num

    return increase()


print(number_increment([1, 2, 3]))
