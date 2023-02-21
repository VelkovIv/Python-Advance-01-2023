from collections import deque

daily_portions = deque(map(int, input().split(", ")))
daily_stamina = deque(map(int, input().split(", ")))
daily_power = 0

conquered_peaks = []

# list level difficulty list as Value 0 peak name, False/True clime or not
peaks_to_conquered = deque(['Vihren', 'Kutelo', 'Banski Suhodol', 'Polezhan', 'Kamenitza'])
peaks_difficulty = deque([80, 90, 100, 60, 70])

for day in range(7):

    if not peaks_to_conquered:
        break

    daily_power = daily_portions.pop() + daily_stamina.popleft()
    difficulty = peaks_difficulty.popleft()
    if daily_power >= difficulty:
        conquered_peaks.append(peaks_to_conquered.popleft())

    else:
        peaks_difficulty.appendleft(difficulty)

if not peaks_to_conquered:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if conquered_peaks:
    print(f'Conquered peaks:')
    print("\n".join(conquered_peaks))
