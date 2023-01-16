longest_intersection = {}

for _ in range(int(input())):
    first_range, second_range = input().split('-')
    first_range_left, first_range_right = first_range.split(',')
    second_range_left, second_range_right = second_range.split(',')

    first_set = set(range(int(first_range_left), int(first_range_right) + 1))
    second_set = set(range(int(second_range_left), int(second_range_right) + 1))

    intersection = first_set.intersection(second_set)
    if len(longest_intersection) < len(intersection):
        longest_intersection = intersection

print(f"Longest intersection is "
      f"[{', '.join(str(el) for el in longest_intersection)}] with length {len(longest_intersection)}")