class Complex:
    def __init__(self, partiereelle, partieimag):
        self.__partier = partiereelle
        self.__partiei = partieimag

    def __add__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__partier+other.__partier, self.__partiei+other.__partiei)
        else: print("Les 2 objets doivent être de la même class")

    def __sub__(self, other):
        if isinstance(other, Complex):
            return Complex(self.__partier-other.__partiei, self.__partiei-other.__partiei)
        else: print("Les 2 objets doivent être de la même class")

    def __mul__(self, other):
         if isinstance(other, Complex):
             return Complex(self.__partier*other.__partier-self.__partiei*other.__partiei, self.__partier*other.__partiei+other.__partier*self.__partiei)
         else: print("Les 2 objets doivent être de la même class")

    def __truediv__(self, other):
        if isinstance(other, Complex):
            return Complex((self.__partier*other.__partier+self.__partiei*other.__partiei)/((other.__partier**2)+(other.__partiei**2)),(self.__partier*other.__partiei+self.__partiei*other.__partier/((other.__partier**2)+(other.__partiei**2))))
        else: print("Les 2 objets doivent être de la même class")

    def __abs__(self):
        return (self.__partier**2+self.__partiei**2)**1/2

    def __eq__(self, other):
         if isinstance(other, Complex):
             return self.__partier == other.__partier and self.__partiei == other.__partiei
         else: print("Les 2 objets doivent être de la même class")

    def __ne__(self, other):
        if isinstance(other, Complex):
            return self.__partiei != other.__partiei and self.__partier != other.__partier
        else: print("Les 2 objets doivent être de la même class")

    def __str__(self):
        return str(self.__partier)+"+"+str(self.__partiei)+"i"

if __name__  == '__main__':

    C1 = Complex(4,2)
    C2 =  Complex(4,2)
    C3 = C1 + C2
    C4 = C1 * C2
    C5 = C1 / C2
    C6 = C1 == C2
    print(C6)



