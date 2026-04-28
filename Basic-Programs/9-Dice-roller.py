# ● ┌ ─ ┐ │ └ ┘

import random

dice_art = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),
    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),
    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),
    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),
    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),
    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
}
dice = []
total = 0
# Input validation
while True:
    try:
        num_of_dice = int(input("How many dice?: "))
        if num_of_dice > 0:
            break
        else:
            print("Enter a positive number!")
    except ValueError:
        print("Enter a valid number!")

for die in range(num_of_dice):
    dice.append(random.randint(1,6))

# This loop works but prints dice art vertically
# for die in range(num_of_dice): --->Goes through each index
#     for line in dice_art.get(dice[die]): --->This loop is incharge of printing every tupple
#         print(line)

# This loop prints dice art horizontally
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line], end="")
    print()

for y in dice:
    total += y

print(f"Total: {total}")