def checker():
    try:
        a = int(input("Podaj I liczbę: "))
        b = int(input("Podaj II liczbę: "))
        if a % b == 0:
            print("Pierwsza liczba jest podzielna przez drugą")
        else:
            print("Pierwsza liczba nie jest podzielna przez drugą")
    except ValueError as e:
        print(f"{e} : Podaj liczbę!")

checker()


