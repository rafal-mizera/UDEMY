import itertools as it

def get_factors(x):
    ret_list = []
    for i in range(1, x):
        if x % i == 0:
            ret_list.append(i)
    return ret_list



candidate_list = list(range(1,101))
filtered_list = list(it.filterfalse(lambda x: sum(get_factors(x)) != x, candidate_list))

for item in filtered_list:
    print(f"{item}: {get_factors(item)}")


def check_if_has_dividers(x):

    for i in range(2, x):
        if x % i == 0:
            return True
    else:
        return False

# prime_numbers = list(it.filterfalse(lambda x: check_if_has_dividers(x), range(1, 10000)))
# print(prime_numbers)

prime_numbers = it.islice(it.filterfalse(lambda x: check_if_has_dividers(x), range(10000000)), 10)
print(list(prime_numbers))

