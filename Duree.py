class Duree:

    def __init__(self, hr, min, sec):
        self.__heure = hr
        self.__minute = min
        self.__seconde = sec

    def __add__(self, other):
        return Duree(self.__heure+other.__heure,self.__minute+other.__minute,self.__seconde+other.__seconde)

    def __str__(self):
        while self.__seconde >= 60:
            if self.__seconde-60 >= 0:
                self.__minute += 1
                self.__seconde = self.__seconde - 60
                if self.__minute-60 >= 0:
                    self.__heure += 1
                    self.__minute = self.__minute - 60
        return (str(self.__heure)+"h"+str(self.__minute)+"m"+str(self.__seconde)+"s")

D1 = Duree(2,64,62)
D2 = Duree(1,54,58)
D3 = D1 + D2
print(D3)
