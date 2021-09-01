import csv

text = """Pharma A, Vitamin C,100
Drugstore XYZ,Penicilin, 20, pills
Drugstore ABC,Aspirin,60
Pharma X,Montelukast,10"""



with open('c:/temp/data.csv','w') as file:
    for line in text:
        file.write(line)

with open('c:/temp/data.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    # for row in csvreader:
    #     print('|'.join(row))
    while True:
        try:
            print(next(csvfile))
        except StopIteration:
            break
            


