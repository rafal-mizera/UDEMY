import os
import time

dir = input("Podaj ścieżkę pliku: ")

if not os.path.isdir(dir):
    print("To nie jest poprawna ścieżka pliku!!!")
else:
    file = input("Podaj nazwę pliku: ")
    path = os.path.join(dir,file)
    if not os.path.exists(path):
        print("Ten plik nie istnieje!!!")
    else:
        print(f"Informacje o pliku {path}")
        print("Data ostatniej modyfikacji: ",time.localtime(os.path.getmtime(path)))
        print(f"Rozmiar pliku: {os.path.getsize(path)} B")
        print("Aktualny katalog: ", os.getcwd())
        print("Względna ścieżka pliku: ", os.path.relpath(path))