import os

line = input("Podaj wysokość wynagrodzenia: ")
filepath = input("Podaj ścieżkę pliku: ")

try:
    with open(filepath,"w") as file:
        file.write(line)
        value = int(line)
except FileNotFoundError as e:
    print("Wrong directory------->",e)
except ValueError as e:
    print("Wrong value-------->",e)
finally:
    print("The value saved in file is:",value)

