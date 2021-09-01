import os

with open(r"C:\temp\moj_plik.txt","a") as f:
    for line in range(1,101):
        f.write(str(line))
        f.write("\n")


with open(r"C:\temp\moj_plik.txt","r") as f:
    z_pliku = f.readlines()

print(z_pliku)

