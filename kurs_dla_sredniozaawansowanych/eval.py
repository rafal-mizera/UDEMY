import math

formula = input("Wprowadź działanie: ")

argument_list = []



for i in range (100):
    argument_list.append(i/10)

for x in argument_list:
    print(x,":",eval(formula))


