colors = ['Hearts','Diamonds','Clubs','Spades']
figures = ['Ace','King','Queen','Jack','10','9']

allCards = []

for color in colors:
    for figure in figures:
        card = color + " " + figure
        allCards.append(card)

print(allCards,len(allCards))

import random

random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []

max = len(allCards)
x = 0

while x < max:
    if x % 2 == 0:
        player1.append(allCards[x])
    else:
        player2.append(allCards[x])
    x += 1

print(player1,"\n",player2)

