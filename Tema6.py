from datetime import date

#1.  Clasa Cerc
# Atribute: raza, culoare
#
# Constructor pt ambele atribute
#
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()
print("--------------------------")
print("Exercitiul 1")

class Cerc:
    raza = 1
    culoare = "rosu"

    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare


    def descrie_cerc(self):
        print(f"{self.raza} {self.culoare}")

    def aria(self, raza):
        self.raza = raza
        return self.raza**2*3.14

    def diametru(self,raza):
        self.raza = raza
        return 2*self.raza*3.14


cerc_nou = Cerc(8,"verde")
print(cerc_nou.aria(1))
print(cerc_nou.diametru(1))
print("--------------------------")
print("Exercitiul 2")
# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie() va PRINTA lungime, latime, culoare
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic.
# Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().


class Dreptungi:
    lungime = 0
    latime = 0
    culoare = "alba"

    def __init__(self,lungime,latime,culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere(self):
        print(f"Avem lungimea de {self.lungime}  cu latimea de {self.latime} si culoarea {self.culoare}")

    def aria(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
        formula = self.lungime * self.latime
        return formula

    def perimetru(self,lungime,latime):
        self.lungime = lungime
        self.latime = latime
        formula = 2 * self.lungime + 2 * self.latime
        return formula

    def schimba_culoarea(self,culoare):
        self.culoare = culoare
        return f"Ti ai schimbat culoarea in {self.culoare}"


drept = Dreptungi(6,7,"rosu")
print(drept.aria(2,4))
print(drept.perimetru(2,4))
print(drept.schimba_culoarea("negru"))
print(drept.descriere())


print("--------------------------")
print("Exercitiul 3")
# 3. Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor() pt toate atributele // constructor reprezinta __init__
# Metode:
# descrie() print nume, prenume, salariu
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)


class Angajat:
    nume = None
    prenume = None
    salariu = None

    def __init__(self,nume,prenume,salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere(self):
        print(f" {self.nume}  {self.prenume} are salariul de {self.salariu}")

    def nume_complet(self,nume,prenume):
        self.nume = nume
        self.prenume = prenume
        formula = self.nume + " " + self.prenume
        return formula

    def salariu_lunar(self,salariu):
        self.salariu = salariu
        return self.salariu

    def salariu_anual(self):
        formula = self.salariu * 12
        return formula

    def marire_de_salariu(self,procent):
        self.procent = procent
        self.salariu = self.salariu + (self.salariu * procent / 100)
        return self.salariu

angajat1 = Angajat("Paparuz","Samuel", 1000)
print(angajat1.nume_complet("Paparuz", "Samuel"))
print(angajat1.descriere())
print(angajat1.marire_de_salariu(10))



print("--------------------------")
print("Exercitiul 4")
# 4. Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total “
# Telefon |      7       |       700       | 49000
#
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class Factura:
    seria = "AAB"
    numar = None
    nume_produs = None
    cantitate = None
    pret_buc = None

    def __init__(self, numar, nume_produs, cantitate, pret_buc):
        self.numar = numar
        self.nume_produs = nume_produs
        self.cantitate = cantitate
        self.pret_buc = pret_buc

    def schimba_cantitatea(self, cantitate):
        self.cantitate = cantitate
        return f"Acum ai cantitatea de {self.cantitate}"

    def schimba_pretul(self, pret_buc):
        self.pret_buc = pret_buc
        return f"Noul tau pret este {self.pret_buc}"

    def schimba_nume_produs(self, nume_produs):
        self.nume_produs = nume_produs
        return f"Noul tau nume al produsului este {self.nume_produs}"

    def genereaza_factura(self):
        self.data = date.today()
        self.total = self.cantitate * self.pret_buc
        return f""" 
            Factura seria {self.seria} numar {self.numar}
                     {self.data}            
        Produs | cantitate | pret bucata | Total 
         {self.nume_produs}   |     {self.cantitate}    |      {self.pret_buc}      |  {self.total}"""


factura1 = Factura(100, "gaz", 50, 6)
print(factura1.genereaza_factura())

print("--------------------------")
print("Exercitiul 5")
# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)

class Cont:
    iban = None
    titular_cont = None
    sold = None

    def __init__(self,iban,titular_cont,sold):
        self.iban = iban
        self.titular_cont = titular_cont
        self.sold = sold


    def afisare_sold(self):
        return f"Titularul {self.titular_cont} are in contul {self.iban} suma de {self.sold} lei"

    def debitare_cont(self, suma):
        self.suma = suma
        self.sold = self.sold + self.suma
        return f"Ai alimentat cu {self.suma} de lei"

    def creditare_cont(self,suma):
        self.suma = suma
        if self.suma <= self.sold:
            self.sold = self.sold - self.suma
            return f"A-ti retras suma de  {self.suma} de lei"
        else:
            return "Nu ai suficienti bani in cont"



ilinca = Cont("RO0001", "Paparuz Ilinca",20000)
print(ilinca.afisare_sold())
print(ilinca.debitare_cont(20000))
print(ilinca.afisare_sold())
print(ilinca.creditare_cont(10000))
print(ilinca.afisare_sold())

print("--------------------------")
print("Exercitiul 5")
# 6. Clasa Masina
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
# Constructor: model, viteza_maxima
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0


class Masina:
    marca = "Dacia"
    model = "Logan"
    viteza_maxima = None
    viteza_actuala = 0
    culoare = "gri"
    culori_disponibile = ("rosu","galben","albastru","verde","roz")
    inmatriculata = False

    def __init__(self, model, viteza_maxima):
        self.model = model
        self.viteza_maxima = viteza_maxima

    def descriere(self):
        return f"""Masina este {self.marca} modelul {self.model} atinge viteza maxima de {self.viteza_maxima},
viteza actuala a masinii este {self.viteza_actuala} si are culoare {self.culoare} . Statusul de inmatriculata este {self.inmatriculata}"""

    def inmatriculare(self):
        if self.inmatriculata == False:
            self.inmatriculata = True
            return self.inmatriculata
        else:
            return "Masina este inmatriculata"

    def vopseste(self,culoare):
        self.culoare = culoare
        if self.culoare in self.culori_disponibile:
            return f"Va  vopsim masina in {self.culoare}"
        else:
            return f" Nu avem aceasta culoare {self.culoare}"

    def accelereaza(self,viteza_actuala):
        self.viteza_actuala = viteza_actuala
        if self.viteza_actuala < 0:
            return "Viteza negativa"
        if self.viteza_actuala > self.viteza_maxima:
            self.viteza_actuala = self.viteza_maxima
            return f"Mergi cu {self.viteza_maxima} Nu poti avea o viteza mai mare decat {self.viteza_maxima}"
        else:
            return f"Acum ai viteza de {self.viteza_actuala}"

    def franeaza(self):
        self.viteza_actuala = 0
        return f"Ai franat ! Acum stai pe loc ai {self.viteza_actuala} "

masina1 = Masina("Sandero", 250)
print(masina1.inmatriculare())
print(masina1.accelereaza(90))
print(masina1.viteza_actuala)
print(masina1.descriere())
print(masina1.inmatriculare())
print(masina1.viteza_actuala)

 # 7. Clasa TodoList
 # Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
 # La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in functie de numele taskului, printam detalii suplimentare daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict
class TodoList:
    todo = {}
    def adauga_task(self, nume, descriere):
        self.todo[nume] = descriere
    def finalizeaza_task(self, nume):
        self.todo.pop(nume)
    def afiseaza_todo_list(self):
        print(list(self.todo.keys()))
    def afiseaza_detalii_suplimentare(self, nume_task):
        if nume_task in self.todo.keys():
            return f"{nume_task} se afla in {self.todo}"
        else:
            print(nume_task, "nu e in todolist, doriti sa adaugati? :")
            if input() == "da":
                self.todo[nume_task] = input("Adaugati descrierea :")
                return self.todo
            else:
                print("la revedere")

todolist1 = TodoList()
todolist1.adauga_task("joi", "fotbal")
todolist1.adauga_task("marti", "munca")
todolist1.adauga_task("luni", "teme")
print(todolist1.todo)
todolist1.finalizeaza_task("joi")
print(todolist1.todo)
print(todolist1.afiseaza_detalii_suplimentare("marti"))