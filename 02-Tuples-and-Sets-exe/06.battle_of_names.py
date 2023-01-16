odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    sum_of_ascii_chr = sum(ord(ch) for ch in input())

    sum_of_ascii = int(sum_of_ascii_chr / row)

    if sum_of_ascii % 2 == 0:
        even_set.add(sum_of_ascii)
    else:
        odd_set.add(sum_of_ascii)

if sum(odd_set) == sum(even_set):
    union_set = odd_set.union(even_set)
    print(*union_set, sep=", ")
elif sum(odd_set) > sum(even_set):
    intersection_set = odd_set.difference(even_set)
    print(*intersection_set, sep=", ")
elif sum(odd_set) < sum(even_set):
    symmetric_diff = even_set.symmetric_difference(odd_set)
    print(*symmetric_diff, sep=", ")
