def double(x):
    return 2 * x


def root(x):
    return x ** 2


def negative(x):
    return -x


def div2(x):
    return x / 2

def GenerateValues(operation,list_of_args):
    result = []
    for x in list_of_args:
        result.append(operation(x))
    return result

x_table = list(range(11))

print(GenerateValues(double, x_table))
print(GenerateValues(div2, x_table))
print(GenerateValues(root, x_table))

