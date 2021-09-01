import os

# webaddresses = []
#
#
#
# while True:
#     line = input("Wprowadź adres strony www lub X by zakończyć: ")
#     if line == "X":
#         break
#     webaddresses.append(line)
#
# dirname = r"C:\temp\data_input"
# filename = input("Podaj nazwę pliku: ")
# filepath = os.path.join(dirname,filename)
#
# with open(filepath,"w") as file:
#     for address in webaddresses:
#         file.write(address + "\n")

############################################################################################################
filename = input("Podaj nazwę pliku: ")

while not os.path.isfile(filename):
    filename = input("Podaj poprawną nazwę pliku!!!: ")


webaddresses = []

with open(filename,"r") as file:
    for line in file:
        line = line.replace("\n","")
        print(line)
        webaddresses.append(line)

# for address in webaddresses:
#     if address.endswith(".pl"):
#         address = f"Adres {address.replace('.pl','')} jest adresem z Polski"
#     else:
#         address = f"Adres {address} nie jest adresem z Polski"
#     print(address)

dirname = os.path.dirname(filename)
websPathPL = os.path.join(dirname,'webs_pl.txt')
websPathOther = os.path.join(dirname,'webs_other.txt')
filePL = open(websPathPL,"w")
fileOther = open(websPathOther,"w")

for line in webaddresses:
    if line.endswith(".pl"):
        filePL.write(line + "\n")
    else:
        fileOther.write(line + "\n")

filePL.close()
fileOther.close()


