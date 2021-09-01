nazwiska = ["jan kot", 18, "ANNA KRÓL", "jÓzeF BYK", ["nie", "wasza", "sprawa"], "ROBERT wĄż" ]
nazwiska = list(filter(lambda x: x is str(x), nazwiska))
print(nazwiska)

nazwiska = list(map(lambda x: x.title() , nazwiska))
print(nazwiska)