stack = input().split(" ")
revert_stack = ""
for i in range(len(stack)):
    revert_stack += stack.pop() + " "
print(revert_stack)