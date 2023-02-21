from collections import deque

males = [int(el) for el in input().split()]
females = deque([int(el) for el in input().split()])

matches = 0
reversed_males = []
while males and females:
    current_male = males.pop()
    current_female = females.popleft()

    if current_male <= 0:
        females.appendleft(current_female)
        continue
    elif current_female <= 0:
        males.append(current_male)
        continue
    elif current_male % 25 == 0:
        males.pop()
        females.appendleft(current_female)
        continue
    elif current_female % 25 == 0:
        females.popleft()
        males.append(current_male)
        continue

    if current_male == current_female:
        matches += 1
    else:
        males.append(current_male - 2)

print(f"Matches: {matches}")
if males:
    for male in range(len(males)-1,-1,-1):
        reversed_males.append(males[male])
    print(f"Males left: {', '.join(map(str, reversed_males) or 'none')}")
else:
    print(f"Males left: none")
print(f"Females left: {', '.join(map(str, females)) or 'none'}")

