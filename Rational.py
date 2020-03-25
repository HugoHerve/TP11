class Rational:
    def __init__(self, num, den):
        self.__numerateur = num
        self.__denominateur = den

    def __add__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerateur*other.__denominateur+other.__numerateur*self.__denominateur,self.__denominateur*other.__denominateur)
        else: print("Les deux objets doivent être de la même class")

    def __sub__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerateur*other.__denominateur-other.__numerateur*self.__denominateur, self.__denominateur*other.__denominateur)
        else: print("Les deux objets doivent être de la même classe")

    def __mul__(self, other):
        if isinstance(other, Rational):
            return Rational(self.__numerateur*other.__numerateur, self.__denominateur*other.__denominateur)
        else: print("Les deux objets doivent être de la même class")

    def __truediv__(self, other):
        if isinstance(other, Rational):
            return (self.__numerateur*other.__denominateur, self.__denominateur*other.__numerateur)
        else: print("Les deux objets doivent être de la même class")

    def PGCD(self,a,b):
        while b != 0:
            r = a%b
            a,b=b,r
        return a

    def __eq__(self, other):
        a = self.PGCD(self.__numerateur, self.__denominateur)
        b = self.PGCD(other.__numerateur,other.__denominateur)
        return (self.__numerateur/a == other.__numerateur/b)and(self.__denominateur/a == other.__denominateur/b)

    def __str__(self):
        if self.__denominateur > self.__numerateur:
            a = self.PGCD(self.__numerateur,self.__denominateur)
            return str(self.__numerateur/a)+"/"+str(self.__denominateur/a)
        else:
            return str(self.__numerateur//self.__denominateur)

if __name__  == '__main__':
    f1 = Rational(1,2)
    f2 = Rational(1,4)
    f8 = Rational(2,4)
    f3 = f1+f2
    f4 = f1-f2
    f5 = f1*f2
    f6 = f1/f2
    f7 = f1 == f8
    print(f1)
    print(f2)
    print(f3)
    print(f4)
    print(f5)
    print(f6)
    print(f7)
