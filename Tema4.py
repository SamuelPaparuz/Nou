
# 1. Avand lista
# masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
#
# Folositi un for ca sa iterati prin toata lista si sa afisati
#  a)‘Masina mea preferata este x’
#  b)Faceti acelasi lucru cu range-ul listei
#  c)Faceti acelasi lucru cu un while

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for cars in masini:
    print(f"Masina mea preferate este un {cars}")
print("-----------------------------------------------")
for cars in range(len(masini)):
    print(f"Masina mea preferata este un {masini[cars]}")

print("-----------------------------------------------")
marca = 0
while marca < len(masini):
    print(f"Masina mea preferata este un  {masini[marca]}")
    marca = marca +1

print("-----------------------------------------------")
# 2. Aceeasi lista
# Folositi un for else
# In for  Modificati elementele din lista astfel incat sa fie scrie cu majuscule, exceptand primul si ultimul
# In else !   Printati lista
masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']
majuscule = len(masini)-1
for index in range(len(masini)):
    if index == 0:
        continue
    if index == majuscule:
        continue
    masini[index] = masini[index].upper()
print(masini)

print("-----------------------------------------------")
# 3 Aceeasi lista,
# Vine un cumparator care doreste sa cumpere un Mercedes ! Iterati prin ea prin modalitatea aleasa de voi
# Daca masina e mercedes Printam ‘am gasit masina dorita de dvs’   Iesim din ciclu folosind un cuvant cheie care face acest lucru
# Altfel  Printam Am gasit masina X. Mai cautam	!


for masina in masini:
    if masina == "Mercedes":
        print(f"Am gasit masina dorita de dvs {masina}! ")
        break
    else:
        print(f"Am gasit masina {masina} Mai cautam !")

print("-----------------------------------------------")
# 4. Aceasi lista! Vine un cumparator bogat dar indecis. Ii vom prezenta toate masinile cu exceptia Trabant si Lastun !

masini = ['Audi', 'Volvo', 'BMW', 'Mercedes', 'Aston Martin', 'Lastun', 'Fiat', 'Trabant', 'Opel']

for masina in masini:
    if masina == "Trabant":
        continue
    if masina == "Lastun":
        continue
    else:
        print(f"Ar putea sa va placa masina  {masina}")


print("-----------------------------------------------")
# 5. Modernizati parcul de masini  !
# Creati o lista goala, masini_vechi
# Iterati prin masini
# Cand gasiti Lastun sau Trabant:
# Salvati aceste masini in masini_vechi
# Suprascrieti-le cu ‘Tesla’ (in lista initiala de masini)
# Printati Modele vechi: x
# Modele noi: x

masini_vechi = []

for masina in masini:
    if masina == "Trabant":
        masini_vechi.append(masina)
    if masina == "Lastun":
        masini_vechi.append(masina)
masini[masini.index("Trabant")] = "Tesla"
masini[masini.index("Lastun")] = "Tesla"
print(f"Modelele vechi de masini sunt {masini_vechi}")
print(f"Modelele noi de masini sunt {masini}")

print("-----------------------------------------------")

# 6.  Avand dict
# pret_masini = {
#     'Dacia': 6800,
#     'Lastun': 500,
#     'Opel': 1100,
#     'Audi': 19000,
#     'BMW': 23000
# }
# Vine un client cu un buget de 15000 euro
# Prezentati doar masinile care se incadreaza in acest buget
# Iterati prin dict.items() si accesati masina si pretul
# Printati Pentru un buget de sub 15000 euro puteti alege masina xLastun
# Iterati prin lista
# Daca masina e Trabant sau Lastun
#  Folositi un cuvant cheie care sa dea skip la ce urmeaza (nu trebuie else)
# Printati S-ar putea sa va placa masina x
pret_masini = {
     'Dacia': 6800,
     'Lastun': 500,
     'Opel': 1100,
     'Audi': 19000,
     'BMW': 23000
 }
buget = 15000
pret = list(pret_masini.values())
i = 0
for masinuta in pret_masini.keys():
    if int(pret[i]) <= buget:
        print(f"Pentru un buget de {buget} euro puteti alege masina {masinuta} care costa {pret[i]}")
        i += 1
print("-----------------------------------------------")
 # 7. Avand lista  numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3] Iterati prin ea Afisati de cateori apare 3
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
count = 0
for i in numere:
    if i == 3:
        count += 1
print(count)
print("-----------------------------------------------")
# 8.  Aceeasi lista
# Iterati prin ea
# Calculati si afisati suma numerelor
# (nu aveti voie sa folositi sum)
total = 0
for suma in numere:
    total += suma
print(total)
print("-----------------------------------------------")
# 9.  Aceeasi lista
# Iterati prin ea
# Afisati cel mai mare numar
# (nu aveti voie sa folositi max)
mare = numere[0]
for x in numere:
    if x > mare:
        mare = x
print(mare)
print("-----------------------------------------------")
# 10. Aceeasi lista
# Iterati prin ea
# Daca numarul e pozitiv, inlocuiti-l cu valoarea lui negativa
# Ex: daca e 3, sa devina -3
# Afisati noua lista
numere = [5, 7, 3, 9, 3, 3, 1, 0, -4, 3]
inversate = []
for i in numere:
    if i <= 0:
        i = i
        inversate.append(i)
    if i > 0:
        i = i - i - i
        inversate.append(i)
print(inversate)

print("-----------------------------------------------")

# 11.alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
# numere_pare = []
# numere_impare = []
# numere_pozitive = []
# numere_negative = []
# Iterati prin lista alte_numere
# Populati corect celelalte liste
# Afisati cele 4 liste la final

alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
numere_pare = []
numere_impare = []
numere_pozitive = []
numere_negative = []

for nr in alte_numere:
    if nr % 2 == 0:
        numere_pare.append(nr)
    if nr % 2 != 0:
        numere_impare.append(nr)
    if nr > 0:
        numere_pozitive.append(nr)
    if nr < 0:
        numere_negative.append(nr)

print(numere_pare)
print(numere_impare)
print(numere_pozitive)
print(numere_negative)
print("-----------------------------------------------")
# 12. Aceeasi lista ! Ordonati crescator lista fara sa folositi sort
# Va puteti inspira vizual de aici  https://www.youtube.com/watch?v=lyZQPjUT5B4
alte_numere = [-5, 7, 2, 9, 12, 3, 1, -6, -4, 3]
lista_noua = []
for i in range(len(alte_numere)):
    a = min(alte_numere)
    lista_noua.append(a)
    alte_numere.remove(a)
print(lista_noua)


print("-----------------------------------------------")
# 13. Ghicitoare de numar
# numar_secret = Generati un numar random intre 1 si 30
# Numar_ghicit = None
# Folosind un while
#    User alege un numar
#    Programul ii spune:
# Nr secret e mai mare
# Nr secret e mai mic
# Felicitari! Ai ghicit!

import random

numar_secret = random.randint(1, 30)
numar_ghicit = None
while numar_secret != numar_ghicit:
    numar_ghicit = int(input("Alege un numar : "))
    if numar_secret > numar_ghicit:
        print("Numar este mai mare")
    elif numar_secret < numar_ghicit:
        print("Numarul este mai mic")
    else:
        print("Felicitari! Ai ghicit!")

print("-----------------------------------------------")

# 14.  Alegeti un numar de la tastatura
# Ex:7
# Scrieti un program care sa genereze in consola urmatoarea piramida
# 1
# 22
# 333
# 4444
# 55555
# 666666
# 7777777
# Ex:3
# 1
# 22
# 333

numar = input("Cate linii vrei sa scrii ? :")
numar = int(numar)
k = 1
while k <= numar:
    line = ""
    for j in range(1, k + 1):
        line = line + str(k)
    print(line)
    k += 1

print("-----------------------------------------------")
# 15. tastatura_telefon = [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9],
#   [0]
# ]
# Iterati prin lista 2d
# Printati ‘Cifra curenta este x’
# (hint: nested for - adica for in for)

tastatura_telefon = [
   [1, 2, 3],
   [4, 5, 6],
   [7, 8, 9],
   [0]
]
tel = []
for i in tastatura_telefon:
    for cifra in i:
        tel.append(cifra)
for k in range(len(tel)):
    print(f"Cifra curenta este {k}")

print("-----------------------------------------------")

