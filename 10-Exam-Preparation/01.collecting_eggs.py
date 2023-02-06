from collections import deque

eggs = deque(map(int, input().split(', ')))
paper = deque(map(int, input().split(', ')))

box_size = 50
fulfil_boxes = 0

while eggs and paper:
    current_egg = eggs.popleft()

    if current_egg <= 0:
        continue
    elif current_egg == 13:
        paper[0], paper[-1] = paper[-1], paper[0]
        continue

    current_paper = paper.pop()

    if current_egg + current_paper <= box_size:
        fulfil_boxes += 1

if fulfil_boxes > 0:
    print(f'Great! You filled {fulfil_boxes} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if paper:
    print(f'Pieces of paper left: {", ".join(map(str, paper))}')