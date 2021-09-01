import math, time

formulas_list = [
    "abs(x**3 - x**0.5)",
    "abs(math.sin(x) * x**2)"
]

argument_list = []
for i in range(100000):
    argument_list.append(i / 10)

for formula in formulas_list: 
    result_list = []
    print(formula)
    start = time.time()
    for x in argument_list:
        result = eval(formula)
        result_list.append(result)
        stop = time.time()

print(min(result_list),"----",max(result_list))
print("Processing time:",stop - start)

for formula in formulas_list:
    result_list = []
    print(formula)
    compiled_formula = compile(formula,formula,"eval")
    start = time.time()
    for x in argument_list:
        result_list.append(eval(compiled_formula))
        stop = time.time()
print(min(result_list),"----",max(result_list))
print("Processing time:",stop - start)





