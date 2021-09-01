x = "myszyydokazujągdykotanieczują"
licznik = {}

for litera in x:
    if litera not in licznik.keys():
        licznik[litera] = 1
    else:
        licznik[litera] += 1

print(licznik)

for key,value in licznik.items():
    if value == 1:
        print(f"Litera - {key} wystąpiła {value} raz")
    else:
        print(f"Litera - {key} wystąpiła {value} razy")




if 4 in licznik.values():
    print(True)
else:
    print(False)

