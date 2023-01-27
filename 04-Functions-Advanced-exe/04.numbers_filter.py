def even_odd_filter(**nums):
    if 'odd' in nums:
        nums['odd'] = [x for x in nums['odd'] if x % 2 != 0]

    if 'even' in nums:
        nums['even'] = list(filter(lambda x: x % 2 == 0, nums['even']))

    return dict(sorted(nums.items(), key=lambda x: -len(x[1])))


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))
