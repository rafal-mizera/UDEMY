class Pies:
    def __init__(self,rasa,imie):
        self.rasa = rasa
        self.imie = imie
    def __str__(self):
        return f"To jest {self.imie} i jest to {self.rasa}"

maly_pies = Pies("ratlerek","Pikuś")
print(maly_pies)
