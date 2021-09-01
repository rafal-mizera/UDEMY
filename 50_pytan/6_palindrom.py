#sprawdź czy poniższe słowo jest palindromem
x = "anakonda"

def czy_palindrom(x):
    if list(x) == list(reversed(x)):
        return True
    else:
        return False

print(czy_palindrom(x))


# print(True if list(x) == list(reversed(x)) else False )

liczba = 121
liczba = str(liczba)
print(liczba)
print(czy_palindrom(liczba))


