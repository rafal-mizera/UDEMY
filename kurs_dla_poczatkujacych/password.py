import random

min = 1
max = 6

dice = random.choice(range(min,max))

if dice == 1:
    print("o")
elif dice == 2:
    print("\to\n\no")
elif dice == 3:
    print("\t\to\n\to\no")
elif dice == 4:
    print("o\to\n\no\to")
elif dice == 5:
    print("o\to\n  o\no\to")
elif dice == 6:
    print("o\to\no\to\no\to")

dices = []
x = 0

while x < 5:
    dice = random.choice(range(min, max))
    dices.append(dice)
    x += 1

print(dices)