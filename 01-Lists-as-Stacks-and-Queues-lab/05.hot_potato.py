from collections import deque

kids_q = deque(input().split(" "))
number = int(input())

while len(kids_q) > 1:
    for i in range(number -1):
        kids_q.append(kids_q.popleft())
    print(f"Removed {kids_q.popleft()}")
print(f"Last is {kids_q.popleft()}")
