data = input()
indexes_parentheses = []

for i in range(len(data)):
    ch = data[i]
    if ch == "(":
        indexes_parentheses.append(i)
    elif ch == ")":
        left = indexes_parentheses.pop()
        print(data[left:i+1])
