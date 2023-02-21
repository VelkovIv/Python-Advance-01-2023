from collections import deque

ramen_bowls = deque(list(map(int, input().split(', '))))
customers = deque(list(map(int, input().split(', '))))

while ramen_bowls and customers:
    current_ramen = ramen_bowls.pop()
    current_customer = customers.popleft()

    if current_ramen > current_customer:
        current_ramen -= current_customer
        ramen_bowls.append(current_ramen)
    elif current_ramen < current_customer:
        current_customer -= current_ramen
        customers.appendleft(current_customer)

if not customers:
    print("Great job! You served all the customers.")
    if ramen_bowls:
        print(f"Bowls of ramen left: {', '.join(map(str, ramen_bowls))}")
else:
    print("Out of ramen! You didn't manage to serve all customers.")
    print(f"Customers left: {', '.join(map(str,customers))}")