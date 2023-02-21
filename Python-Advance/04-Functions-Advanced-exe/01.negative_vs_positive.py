def print_func(positive, negative):
    print(sum(negative))
    print(sum(positive))

    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = list(map(int, input().split()))

positive_numbers = [n for n in numbers if n > 0]
negative_numbers = [n for n in numbers if n < 0]

print_func(positive_numbers, negative_numbers)
