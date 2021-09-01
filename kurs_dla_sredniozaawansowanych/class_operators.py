class Cake:
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def __str__(self):
        return f"{self.kind}|{self.name} with {self.additives} and filled with {self.filling}"

    def __iadd__(self, other):
        if type(other) == str:
            self.additives.append(other)
            return self
        elif type(other) == list:
            self.additives.extend(other)
            return self
        else:
            raise Exception(f"Sorry this method not implemented for {type(other)}")


    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print('-' * 20)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')

print(cake01)

cake01 += ["Caramel","Salt"]
print(cake01)