import numpy as np
class Matrice:
    def __init__(self, elements = []):
        if len(elements) != 4:
            print("La matrice a besoin de 4 variables")
        else :
            self.__data = elements

    def __add__(self, other):
        liste = [self.__data[0]+other.__data[0],self.__data[1]+other.__data[1],self.__data[2]+other.__data[2],self.__data[3]+other.__data[3]]
        return Matrice(liste)

    def __sub__(self, other):
        liste = [self.__data[0]-other.__data[0],self.__data[1]-other.__data[1],self.__data[2]-other.__data[2],self.__data[3]-other.__data[3]]
        return Matrice(liste)

    def __mul__(self, other):
        liste = [self.__data[0]*other.__data[0]+self.__data[1]*other.__data[2],self.__data[0]*other.__data[1]+self.__data[1]*other.__data[3],self.__data[2]*other.__data[0]+self.__data[3]*other.__data[2],self.__data[2]*other.__data[1]+self.__data[3]*other.__data[3]]
        return Matrice(liste)
    def __str__(self):
        return ("["+str(self.__data[0])+","+str(self.__data[1])+"]"+'\n'
               "["+str(self.__data[2])+","+str(self.__data[3])+"]"+'\n'
                "-----------")



if __name__  == '__main__':

    M1 = Matrice([1,2,3,4])
    M2 = Matrice([1,2,3,4])
    M3 = M1+M2
    M4 = M1*M2
    print(M3)
    print(M4)

