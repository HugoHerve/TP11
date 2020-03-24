class  Cercle:
    def __init__(self, rayon):
        self.__rayon = rayon

    def __add__(self, other):
        if isinstance(other, Cercle):
            return Cercle(self.__rayon + other.__rayon)
        else: print("Les 2 objets doivent être de la même class")
    def __lt__(self, other):
        if isinstance(other, Cercle):
            return self.__rayon < other.__rayon
        else:print("Les 2 objets doivent être de la même class")

    def __gt__(self, other):
        if isinstance(other, Cercle):
            return self.__rayon > other.__rayon
        else:print("Les 2 objets doivent être de la même class")

    def __str__(self):
        return ("Cerlce de rayon"+ str(self.__rayon))


if __name__  == '__main__':
    c1 = Cercle(2)
    c2 = Cercle(3)
    c3 = c1 + c2
    c4 = c1 < c2
    c5 = c2 > c3
    print(c3)
