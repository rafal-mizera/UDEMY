jezyki = ["Python","Ruby","#C","Java"]
jezyki_odwrocona = list(reversed(jezyki))
print(jezyki_odwrocona)

jezyki.reverse()
print(jezyki)

jezyki = ["Python","Ruby","C#","Java"]

jezyki_odwrocona = jezyki[::-1]
print(jezyki_odwrocona)

jezyki_odwrocona = []

for jezyk in jezyki:
    jezyki_odwrocona.insert(0,jezyk)
