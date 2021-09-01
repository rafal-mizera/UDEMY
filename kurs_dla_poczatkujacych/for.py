data = ['Error:File cannot be open',
        'Error:No free space on disk',
        'Error:File missing',
        'Warning:Internet connection lost',
        'Error:Access denied']

elements = []

for el in data:
    elements = list(el.split(":"))
    if elements[0] == "Error":
        print(elements[0].upper(),elements[1].upper())
    else:
        print(elements[0].upper(), elements[1])

string_A = '+---+---+---+---+'
string_B = '|   |   |   |   |'

for num in range(1,10):
    if num % 2 != 0:
        print(string_A)
    else:
        print(string_B)

for num in range(1,10):
    if num % 2 == 0:
        print(num * "x")
    else:
        print(num * "o")


#####################################################
"""W tym zadaniu obliczysz silnię. Silnia  to działanie matematyczne, 
które dla liczby n wyznacza wartość mnożąc przez siebie wszystkie liczby naturalne mniejsze
 lub równe n. Symbol oznaczający silnię to wykrzyknik, np.:"""

i = 10

for x in range(1,i+1):
    result = 1
    for j in range(1,x+1):
        result *= j

    print(x,result)

def silnia(x):
    if x == 0:
        return 1
    elif x < 0:
        return "Nie można wyświetlić silni"
    else:
        return x * silnia(x-1)


list_noun = ['dog', 'potato', 'meal', 'icecream', 'car']
list_adj = ['dirty', 'big', 'hot', 'colorful', 'fast']

for noun in list_noun:
    for adj in list_adj:
        print(adj + " " + noun)



print(4,silnia(4))



