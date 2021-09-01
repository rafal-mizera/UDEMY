lista = [12,0,4,1,24,19,400,341,56,89]
lista = sorted(lista)

szukana = 1000
l = 0
p = len(lista) - 1

while l <= p:
    s = (l+p) // 2
    if lista[s] == szukana:
        print("Szukana liczba jest na liście")
        break
    elif lista[s] < szukana:
        l = s + 1
        print(".")
    else:
        p = s - 1
        print(".")
else:
    print("Szukanej liczby nie ma na liście")