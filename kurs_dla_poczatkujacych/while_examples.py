x = 50
y = 0

while y < 50:
    print(y," + ",y+1,"= ",y + y + 1)
    y +=1

######################################################################
import random
my_number = random.randint(0,20)

print("Zgadnij liczbę")

guess = -1
x = 0

while guess != my_number:
    guess = int(input("Podaj liczbę od 0 do 20: "))
    x += 1
    if guess > my_number:
        print("Szukana liczba jest mniejsza")
    elif guess < my_number:
        print("Szukana liczba jest większa")
    else:
        print(f"Brawo, odgadłeś liczbę w próbie nr {x}")
