text_list = ['x','xxx','xxxxx','xxxxxxx','']

f = lambda x: len(x)

print(f("traktor"))

print(list(map(lambda x: len(x),text_list)))