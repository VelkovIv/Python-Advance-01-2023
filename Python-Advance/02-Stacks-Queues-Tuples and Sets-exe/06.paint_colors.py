from collections import deque

data = deque(input().split())

all_colors = {"red", "yellow", "blue", "orange", "purple", "green"}
secondary_colors = {
    "orange": ["red", "yellow"],
    "purple": ["red", "blue"],
    "green": ["yellow", "blue"]

}

found_colors = []

while data:
    first_str = data.popleft()
    second_str = data.pop() if data else ''

    if first_str + second_str in all_colors:
        found_colors.append(first_str + second_str)
    elif second_str + first_str in all_colors:
        found_colors.append(second_str + first_str)
    else:
        for current_str in (first_str[:-1], second_str[:-1]):
            if current_str:
                data.insert(len(data) // 2, current_str)

for color in set(secondary_colors.keys()).intersection(found_colors):
    if not set(secondary_colors[color]).issubset(found_colors):
        found_colors.remove(color)

print(found_colors)