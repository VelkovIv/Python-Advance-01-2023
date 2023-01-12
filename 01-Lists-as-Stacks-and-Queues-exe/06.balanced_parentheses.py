from collections import deque

parentheses = deque(input())

left_parentheses = []

while parentheses:
    current_parentheses = parentheses.popleft()

    if current_parentheses in "([{":
        left_parentheses.append(current_parentheses)
        continue
    elif not left_parentheses:
        print("NO")
        break
    if f"{left_parentheses.pop()}{current_parentheses}" in "{}[]()":
        continue
    else:
        print("NO")
        break
else:
    print("YES")
