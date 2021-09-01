imiona = ["Anna", "Zbigniew", "Michał", "Edward", "Zofia"]

for x,y in enumerate(imiona,1):
    print(x,":",y)

y = 1
for imie in imiona:
    print(f"{y}: {imie}")
    y += 1