class Cake:
    """This class is containing informations about cakes available in our bakery.
    For example: kind,taste,filling etc."""

    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        """This method requires such arguments as name,kind,taste,additives and filling"""

        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

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

    @property
    def full_name(self):
        """This method is returning a formated full name of our product"""

        return "--== {} - {} ==--".format(self.name.upper(), self.kind)


help(Cake)
help(Cake.__init__)
help(Cake.full_name)