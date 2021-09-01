

# file = open(r"C:\temp\data_input\orders\orders.txt")
# content = file.read()

with open(r"C:\temp\data_input\orders\orders.txt","r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        if len(order) == 3:
           print(f"Order from drugstore: {order[0]}, {order[1]}, {order[2]}")
        else:
           print(f"Line:\t {line}\t\t malformed!!!")

    print("Proccesing complete")


