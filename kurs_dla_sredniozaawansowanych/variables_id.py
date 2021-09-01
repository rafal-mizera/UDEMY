a = b = c = 10
a = 20
print(a,id(a))
print(b,id(b))
print(c,id(c))

#########################

d = e = f = [1,2,3]
d.append(4)
print(d,id(d))
print(e,id(e))
print(f,id(f))

##########################

x = 10
y = 10
print(id(x),id(y))

y = y + 1 - 1
print(id(x),id(y))

y = y + 1234567890 - 1234567890
print(id(x),id(y))