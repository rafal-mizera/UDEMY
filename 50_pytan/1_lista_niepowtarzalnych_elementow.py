A = [1,2,3,3,2,1,2,3]

# B = set(A)
# B = list(B)
# print(B)

B = []

for el in A:
    if el not in B:
        B.append(el)

print(B)