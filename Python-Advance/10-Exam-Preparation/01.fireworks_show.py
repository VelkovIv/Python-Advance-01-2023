from collections import deque

fireworks_effects = deque([int(el) for el in input().split(", ")])
explosive_power = [int(el) for el in input().split(", ")]
palm_fireworks = 0
willow_fireworks = 0
crossette_fireworks = 0
is_perfect_show = False

while fireworks_effects and explosive_power:
    current_fireworks_effect = fireworks_effects.popleft()
    current_explosive_power = explosive_power.pop()

    if current_fireworks_effect <= 0:
        explosive_power.append(current_explosive_power)
        continue

    if current_explosive_power <= 0:
        fireworks_effects.appendleft(current_fireworks_effect)
        continue

    current_mixture = current_fireworks_effect + current_explosive_power

    if current_mixture % 3 == 0:
        if current_mixture % 5 == 0:
            crossette_fireworks += 1
        else:
            palm_fireworks += 1

    elif current_mixture % 5 == 0:
        willow_fireworks += 1

    else:
        current_fireworks_effect -= 1
        fireworks_effects.append(current_fireworks_effect)
        explosive_power.append(current_explosive_power)

    if palm_fireworks >= 3 and willow_fireworks >= 3 and crossette_fireworks >= 3:
        is_perfect_show = True
        break

if is_perfect_show:
    print("Congrats! You made the perfect firework show!")
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effects:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effects))}")

if explosive_power:
    print(f"Explosive Power left: {', '.join(map(str, explosive_power))}")

print(f"Palm Fireworks: {palm_fireworks}")
print(f"Willow Fireworks: {willow_fireworks}")
print(f"Crossette Fireworks: {crossette_fireworks}")
