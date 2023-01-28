def math_operations(*nums, **kwargs):
    for num in range(len(nums)):
        key = list(kwargs.keys())[num % 4]

        if key == 'a':
            kwargs['a'] += nums[num]
        elif key == 's':
            kwargs['s'] -= nums[num]
        elif key == 'm':
            kwargs['m'] *= nums[num]
        elif key == 'd' and nums[num] != 0:
            kwargs['d'] /= nums[num]
    result = ''
    for key, value in sorted(kwargs.items(), key=lambda x: (-x[1], x[0])):
        result += f'{key}: {value:.1f}\n'

    return result


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))