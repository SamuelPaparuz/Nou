from abc import ABC, abstractmethod
# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
#
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura
# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de clasa abstracta
#
# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte


class FormaGeometrica(ABC):
    pi = 3.14

    @abstractmethod
    def aria(self):
        pass

    def descrie(self):
        print("Cel mai probabil am colturi")


class Patrat(FormaGeometrica):


    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return self.__latura

    @latura.getter
    def latura(self):
        print(f'Latura este {self.__latura}')

    @latura.setter
    def latura(self, latura):
        print(f'Noua latura este  {latura}')
        self.__latura = latura

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        self.__latura = None

    def aria(self):
        if self.__latura == None:
            print("Pentru a calcula aria iti trebuie o latura valida")
        else:
            aria = self.__latura * self.__latura
            print(f'Aria patratului este {aria}')


class Cerc(FormaGeometrica):

    def __init__(self, __raza):
        self.__raza = __raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza ta este {self.__raza} ')
        return self.__raza

    @raza.setter
    def raza(self, raza):
        self.__raza = raza
        print(f'Noua raza este {raza}')
        return self.__raza

    @raza.deleter
    def raza(self):
        print('Am sters raza')
        self.__raza = None

    def aria(self):
        if self.__raza == None:
            print("Pentru a calcula aria iti trebuie o raza valida")
        else:
            raza = FormaGeometrica.pi * self.__raza * self.__raza
            print(f"Raza cercului este {raza}")

    def descrie(self):
        print("Sunt un cerc...nu am colturi")

patrat1 = Patrat(2)
patrat1.latura = 4
patrat1.aria()
patrat1.descrie()
del patrat1.latura
patrat1.aria()

print("---------------")

cerc1 = Cerc(2)
cerc1.raza
cerc1.raza = 3
del cerc1.raza
cerc1.descrie()
cerc1.aria()

