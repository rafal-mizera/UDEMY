lista = [123,32343,556,57754345,3242565,232323232323,1]

print(sorted(lista,key= lambda x: len(str(x))))


A = [1,2,3]
B = A.copy()

print(id(A),id(B))