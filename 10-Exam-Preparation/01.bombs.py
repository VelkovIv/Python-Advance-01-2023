from collections import deque

bomb_effect = deque(map(int, input().split(', ')))
bomb_casing = deque(map(int, input().split(', ')))

bomb_type = {
    "Datura Bombs": 40,
    "Cherry Bombs": 60,
    "Smoke Decoy Bombs": 120
}
bombs_created = False
created_bomb = {
    "Cherry Bombs": 0,
    "Datura Bombs": 0,
    "Smoke Decoy Bombs": 0
}

while bomb_effect and bomb_casing:
    # if not current_casing:
    current_effect = bomb_effect.popleft()
    current_casing = bomb_casing.pop()

    if current_effect + current_casing >= 120:
        created_bomb["Smoke Decoy Bombs"] += 1
    elif current_effect + current_casing >= 60:
        created_bomb["Cherry Bombs"] += 1
    elif current_effect + current_casing >= 40:
        created_bomb["Datura Bombs"] += 1

    if created_bomb["Cherry Bombs"] >= 3 and created_bomb["Datura Bombs"] >= 3 and created_bomb[
        "Smoke Decoy Bombs"] >= 3:
        bombs_created = True
        break

if bombs_created:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
print(f"Bomb Effects: {', '.join(map(str, bomb_effect)) or 'empty'}")
print(f"Bomb Casings: {', '.join(map(str, bomb_casing)) or 'empty'}")
for bomb, num in created_bomb.items():
    print(f"{bomb}: {num}")
