stack = []
number_of_queries = int(input())

for num in range(number_of_queries):
    current_query = input().split(" ")

    if current_query[0] == "1":
        stack.append(int(current_query[1]))
    elif current_query[0] == "2" and len(stack) > 0:
        stack.pop()
    elif current_query[0] == "3" and len(stack) > 0:
        print(max(stack))
    elif current_query[0] == "4" and len(stack) > 0:
        print(min(stack))

if len(stack) > 0:
    for i in range(len(stack)):
        if len(stack) > 1:
            print(stack.pop(), end=", ")
        else:
            print(stack.pop(), end=" ")
