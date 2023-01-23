lists = input().split("|")
flatten_list = []

for lst in lists[::-1]:
    flatten_list.extend(lst.split())

print(*flatten_list)
