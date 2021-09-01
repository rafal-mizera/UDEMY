import itertools as it
import math

notes = ['C', 'D', 'E', 'F', 'G', 'A', 'B']
i = 1
for combination in it.permutations(notes,4):
    print(combination)
    print(i)
    i += 1

print("4-notes melody, notes cannot repeat - it is variation without repeating - there are {} possibilities".format(
    math.factorial(len(notes))/math.factorial(len(notes) - 4)))

i = 1
for combination in it.product(notes,repeat=4):
    print(combination)
    print(i)
    i += 1


print("4-notes melody - notes can repeat - it is variation with repeating - there are {} possibilities".format(
        pow(len(notes), 4)))

