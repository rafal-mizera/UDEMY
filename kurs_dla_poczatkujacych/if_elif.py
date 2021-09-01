"""Pracujesz dla firmy odzieżowej, której celem jest wypromowanie nowej kolekcji ubrań.
Firma ogłosiła konkurs, który ma na celu zdobywanie "lajków" i "udostępnień" na Facebooku.
Jeśli strona firmy otrzyma danego dnia co najmniej 500 "lajków" i co najmniej 100 "udostępnień",
to ceny spadną o 10%. Na razie masz napisać fragment programu, który rozstrzygnie czy warunki promocji są spełnione czy nie.
 Jeśli już wiesz jak to zrobić "GO ON!",
 a jeśli chcesz, aby Cię trochę pokierować - zajrzyj do kolejnych punktów:"""

min_likes = 500
min_shares = 100
num_likes = 500
num_shares = 10
prices = int


# if num_likes >= min_likes and num_shares >= min_shares:
#     print("Prices are now 10 percent lower!!!")
# else:
#     print("Not enough likes or shares")

if num_likes >= min_likes and num_shares >= min_shares:
    print("Prices are now 10 percent lower!!!")
else:
    if num_likes < min_likes:
        print("You need more likes!")
    else:
        print("You need more shares!")



"""Pracujesz dla restauracji, która chce nagrodzić klientów zamawiających w dni robocze (poza weekendem)
 pizze lub duży napój. Klienci spełniający warunki promocji dostaną kupon na darmowego burgera.
 Na razie piszesz polecenie decydujące o spełnieniu warunków promocji. Do dyspozycji masz zmienne:"""

orderedPizza = True
orderedBigBeverage = True
isWeekend = False

if orderedPizza or orderedBigBeverage and not isWeekend:
    print("You get free Burger")
else:
    print("Please order something more :)")

######################################################################################
musclePain = False
fever = False
weakness = False

if musclePain and fever and weakness:
    print("Suspision of influenza")
elif weakness and not fever or not musclePain:
    print("Just take a rest")
else:
    print("You may be cold")

######################################################################################
CheckCompleted = False

print("Check is complete!" if CheckCompleted else "Check not complete yet")




