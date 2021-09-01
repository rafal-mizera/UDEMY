import random

x = 0

while x < 10:
    print(random.randint(1,100))
    x += 1

################################################3

number1 = random.randint(1,100)
counter = 0
number2 = random.randint(1,100)

while number1 != number2:
    counter += 1
    number2 = random.randint(1,100)
    print("Try nr: ", counter,"Generated nr: ", number2, "my number", number1)
else:
    print(f"It took {counter} tries :)")

#################################################################################################

countries = [
        'Uruguay',
        'Russia',
        'Saudi Arabia',
        'Egypt',
        'Spain',
        'Portugal',
        'Iran',
        'Morocco',
        'France',
        'Denmark',
        'Peru',
        'Australia',
        'Croatia',
        'Argentina',
        'Nigeria',
        'Iceland',
        'Brazil',
        'Switzerland',
        'Serbia',
        'Costa Rica',
        'Sweden',
        'Mexico',
        'Korea Republic',
        'Germany',
        'Belgium',
        'England',
        'Tunisia',
        'Panama',
        'Colombia',
        'Japan',
        'Senegal',
        'Poland'
        ]

random.shuffle(countries)
print(countries)

groupNumber = 0

for i in range(len(countries)):

    if i % 4 == 0:
        groupNumber += 1
        print(f"----GRUPA {groupNumber}----")
    print(countries[i])
