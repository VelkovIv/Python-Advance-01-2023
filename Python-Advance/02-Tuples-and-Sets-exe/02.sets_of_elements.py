first_number, second_number = list(map(int, input().split()))

first_set = {int(input()) for _ in range(first_number)}
second_set = {int(input()) for _ in range(second_number)}

print(*(first_set.intersection(second_set)), sep="\n")
