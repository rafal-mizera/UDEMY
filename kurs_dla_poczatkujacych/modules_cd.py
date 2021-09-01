inputdata = [0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
factortable = [0, 0.01, 0.02, 0.03, 0.05, 0.08, 0.13, 0.21, 0.34, 0.55, 0.89]

import math

print("Inputdata elements :",len(inputdata),"Factortable elements:",len(factortable))

# if len(inputdata) == len(factortable):
#     print("OK")
#     for el in inputdata:
#         minvalue = (el - factortable[inputdata.index(el)]) * el
#         maxvalue = (el + factortable[inputdata.index(el)]) * el
#         mininteger = math.floor(minvalue)
#         maxinteger = math.ceil(maxvalue)
#         print(round(minvalue,2),"\t",round(maxvalue,2))
#         print(mininteger,el,maxinteger)

# else:
#     print("inputdata and factortable need to have equal number of element")

import random

import random
x = random.random()

for el in inputdata:
    minvalue = (el - x) * el
    maxvalue = (el + x) * el
    print(minvalue,maxvalue)

import datetime

print(datetime.datetime.now())
