def sorting_cheeses(**cheeses):
    cheeses = sorted(cheeses.items(), key=lambda x: (-len(x[1]), x[0]))

    result = []

    for cheese, quantities in cheeses:
        result.append(cheese)
        lst = sorted(quantities, reverse=True)
        result.extend(lst)

    return '\n'.join(str(el) for el in result)


print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)