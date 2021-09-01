import sys

file_path = r"C:\temp\data_input\orders\orders.txt"

with open(file_path, "r") as file:
    for line in file:
        line = line.replace('\n', '')
        order = line.split(',')
        try:
            pharmacy_name = order[0]
            item = order[1]
            amount = int(order[2])
            print(f"Order from drugstore {pharmacy_name}: item - {item}, amount {amount} $")
        except ValueError as e:
            print("Please insert correct value------",e)
        except  IndexError as e:
            print("Please correct the item------",e)


        except:
            print(f"Wrong data inserted here: {line} ",sys.exc_info()[0])


print("Processing finished")


