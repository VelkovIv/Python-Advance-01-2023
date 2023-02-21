from collections import deque

food_quantity = int(input())
orders = deque(map(int, input().split(" ")))

print(max(orders))

for i in range(len(orders)):
    if food_quantity >= orders[0]:
        food_quantity -= orders.popleft()

    else:
        break
if not orders:
    print("Orders complete")
else:
    print(f"Orders left: ", end="")
    for _ in range(len(orders)):
        print(orders.popleft(), end=" ")
