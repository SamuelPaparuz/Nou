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
    latura = None


    def __init__(self, latura):
        self.__latura = latura

    @property
    def latura(self):
        return  self.__latura
    @latura.getter
    def latura(self):
        print('Getting latura')
        return self.__latura

    @latura.setter
    def latura(self, value):
        print('Am schimbat latura cu ' + value)
        self.__latura = value

    @latura.deleter
    def latura(self):
        print('Am sters latura')
        del self.__latura

    def aria(self):
        return self.__latura * 4


class Cerc(FormaGeometrica):
    def __init__(self, raza):
        self.__raza = raza

    @property
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print('Getting raza')
        return self.__raza

    @raza.setter
    def raza(self,value):
        print('Am schimbat raza cu ' + value)
        self.__raza = value
        return self.__raza

    @raza.deleter
    def raza(self):
        print('Am sters raza')
        del self.__raza

    def aria(self):
        aria = self.pi + self.__raza
        return aria

    def descrie(self):
        return "Sunt un cerc...nu am colturi"


samy = Cerc(4)
print(samy.aria)
