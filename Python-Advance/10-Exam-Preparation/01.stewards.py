from collections import deque

six_seats = input().split(', ')
first_sequence = deque(map(int, input().split(', ')))
second_sequence = deque(map(int, input().split(', ')))

rotations = 0
seat_matches = []

while len(seat_matches) < 3 and rotations < 10:
    first = first_sequence.popleft()
    second = second_sequence.pop()

    letter = chr(first + second)

    if str(first) + letter in six_seats and str(first) + letter not in seat_matches:
        seat_matches.append(str(first) + letter)

    elif str(second) + letter in six_seats and str(second) + letter not in seat_matches:
        seat_matches.append(str(second) + letter)

    else:
        first_sequence.append(first)
        second_sequence.appendleft(second)

    rotations += 1

print(f'Seat matches: {", ".join(seat_matches)}')
print(f'Rotations count: {rotations}')
