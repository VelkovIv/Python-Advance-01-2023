from _collections import deque

customer_q = deque()
COMMAND_PAID = "Paid"
COMMAND_END = "End"

while True:
    current_input = input()

    if current_input == COMMAND_PAID:
        for i in range(len(customer_q)):
            print(customer_q.popleft())

    elif current_input == COMMAND_END:
        print(f"{len(customer_q)} people remaining.")
        break
    else:
        customer_q.append(current_input)