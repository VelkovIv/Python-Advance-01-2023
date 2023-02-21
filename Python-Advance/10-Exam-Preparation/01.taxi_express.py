from collections import deque

customers = deque(list(map(int, input().split(', '))))
taxis = deque(list(map(int, input().split(', '))))

total_time = 0

while customers and taxis:
    current_customer = customers.popleft()
    current_taxis = taxis.pop()

    if current_customer <= current_taxis:
        total_time += current_customer
    elif current_customer > current_taxis:
        customers.appendleft(current_customer)

if customers:
    print("Not all customers were driven to their destinations")
    print(f'Customers left: {", ".join(map(str, customers))}')
else:
    print("All customers were driven to their destinations")
    print(f'Total time: {total_time} minutes')
