colors = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
figures = [
    {'Figure': 'Ace', 'Power': 14},
    {'Figure': 'King', 'Power': 13},
    {'Figure': 'Queen', 'Power': 12},
    {'Figure': 'Jack', 'Power': 11},
    {'Figure': '10', 'Power': 10},
    {'Figure': '9', 'Power': 9}]

allCards = []

for figure in figures:
    for color in colors:
        aCard = figure.copy()
        aCard["Color"] = color
        allCards.append(aCard)

print(len(allCards))

import random

random.shuffle(allCards)

player1 = []
player2 = []

for card in allCards:
    if allCards.index(card) % 2 == 0:
        player1.append(card)
    else:
        player2.append(card)
while len(player1) > 0 and len(player2) > 0:
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    stock = []

    if card1["Power"] == card2["Power"]:
        player1.append(card1)
        player2.append(card2)
        # print('=EQUAL \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('=EQUAL \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    elif card1["Power"] > card2["Power"]:
        player1.append(card1)
        player1.append(card2)
        # print('PLAY-1 \t %d \t %d \t %d \t %d' % (card1["Power"], card2["Power"], len(player1), len(player2)))
        print('PLAY-1 \t %d \t %d \t' % (card1["Power"], card2["Power"]) + len(player1) * '*')
    else:
        while card1["Power"] == card2["Power"]:
            print("WAR IS ON")
            print(card1["Power"],"VS",card2["Power"])
            stock.append(card1,card2)
            if len(player1) < 2:
                player2.append(stock)
                player2.append(player1)
                player1.clear()
                break
            elif len(player2) < 2:
                player1.append(stock)
                player1.append(player2)
                player2.clear()
                break
            else:
                card1 = player1.pop(0)
                card2 = player2.pop(0)
                stock += card1,card2
                card1 = player1.pop(0)
                card2 = player2.pop(0)




                



if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')


if len(player1) > 0:
    print('PLAYER 1 WON!!!!')
else:
    print('PLAYER 2 WON!!!!')

