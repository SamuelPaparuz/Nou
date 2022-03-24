#                               Tema 1

# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 1 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video cu Variabile si Tipuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video cu Operatori si Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/

# 1, 2, 3 = rezolvat
print(" A. Usor = rezolvat")
print("----------------------------------------------")

# b. Usor spre Mediu (obligatoriu)
# 1. In cadrul unui comentariu, explicati cu cuvintele voastre ce este o variabila
# O variabila este o ca o cutiuta in care punem valorile si va incepe tot timpul cu litera mica ! - stiu ca nu sunt cuvintele mele dar asa o percep dupa intro in programare!
print(" B . Exercitiul 1")
print("O variabila este o ca o cutiuta in care punem valorile si va incepe tot timpul cu litera mica ! - stiu ca nu sunt cuvintele mele dar asa o percep dupa intro in programare ")
print("----------------------------------------------")


# 2.Declarati si initializati cate o variabila din fiecare din urmatoarele tipuri:
# string, int, float, bool
# Valorile le alegeti voi dupa preferinte
print("Exercitiul 2")

nume= "Samy"
varsta = 26
media = 9.33
admis = True

print(nume)
print(varsta)
print(media)
print(admis)

print("----------------------------------------------")


#3.Utilizati functia type pentru a verifica daca au tipul de date asteptat
print("Exercitiul 3")

print(type(nume))
print(type(varsta))
print(type(media))
print(type(admis))

print("----------------------------------------------")
# 4.Rotunjiti float-ul folosind functia round() si salvati aceasta modificare in aceeasi variabila (suprascriere)
# Verificati tipul acesteia
print("Exercitiul 4")

media = round(media)
print(media)
print(type(media))

print("----------------------------------------------")

#5.folositi print() si printati in consola 4 propozitii folosind cele 4 variabile.
#(rezolvati nepotrivirile de tip prin ce modalitate doriti)
print("Exercitiul 5")

print(f"Eu sunt {nume} si am {varsta} ani")
print(f"{nume} a avut media {media} si are {varsta} ani")
print(f"Avand media {media} sunt declarat admis la facultate {admis}")
print(f"{nume} are {varsta} de ani si are {media} ca medie deci poate da la facultate {admis}" )
# e 9 ca medie deoarece am suprascris cu round

print("----------------------------------------------")

#6. Citeste de la tastatura numele
# citeste de la tastatura prenumele
# afiseaza 'Numele complet are x caractere'
print("Exercitiul 6")

nume1 = input("Numele :")
prenume = input("Prenumele :")
nume_complet = len(nume1 + prenume)
print(f"{nume1} {prenume} are {nume_complet} caractere")

print("----------------------------------------------")

# 7 citeste de la tastatura lungimea
# citeste de la tastatura latimea
# afiseaza 'Aria dreptunghiului este x'
print("exercitiul 7")
l = int(input("Lungimea :"))
lat = int(input("Latimea :"))
ar = l * lat
print(f"Aria dreptunghiului este {ar}")


print("----------------------------------------------")
# 8.Avand stringul: 'Coral is either the stupidest animal or the smartest rock'
# cititi de la tastatura un int x
# afiseaza stringul fara ultimele x caractere
print("Exercitiul 8")

coral = "Coral is either the stupidest animal or the smartest rock"
coral1 = int(input("Numar :"))
print(coral1[:-4])

print("----------------------------------------------")

# 9.acelasi string
# declara un string nou care sa fie format din primele 5 caractere + ultimele 5
print("Exercitiul 9")

nou = " trebuie sa trec tot in input "
print(nou[0:5] + nou[-5:])

print("----------------------------------------------")
# 10.acelasi string
# afisati de cate ori apare cuvantul 'the'
print("exercitiul 10")

print(coral.count("the"))  # 3 ...ele normal sunt 2 dar se calculeaza si either

print("----------------------------------------------")

# 11.acelasi string
# inlocuieste the cu THE peste tot
# printeaza rezultatul
print("Exercitiul 11")

coral = coral.replace("the", "THE")
print(coral)

print("----------------------------------------------")

# 12.acelasi string
# salveaza intr-o variabila si afiseaza indexul de start al cuvantului rock
# (hint: este o functie care te ajuta sa faci asta)
# folosind aceasta variabila + slicing, afiseaza tot stringul pana la acest cuvant
# output: 'Coral is either the stupidest animal or the smartest '
print("Exercitiul 12")

piatra = coral.find("rock")
print(piatra)
print(coral[0:piatra])



print("----------------------------------------------")
# 13.Folosind variabilele definite la exercitiul numarul 2 (cele 4 variabile declarate de tip str, int, float, bool),
# declarati o alta variabila de tip string in care sa le adaugati folosind tehnica de formatare a unui string.
# Printeaza rezultatul
print("Exercitiul 13")
cutie = f"{nume}, {varsta}, {media}, {admis}"
print(cutie)

print("----------------------------------------------")
#14 .avand stringul '0123456789' afisati doar numerele pare ,acum afisati doar numerele impare
# (hint: folositi slicing, controlati din pas)
print("Exercitiul 14")

numere = "0123456789"
print(f" Nr pare : {numere[::2]}")
print(f" Nr impare: {numere[1::2]}")

print("----------------------------------------------")

#15 Aveti un dreptunghi, declarati 2 variabile pe nume “lungime” si “latime”, ele trebuie sa primeasca ca si input de la
# tastatura dimensiunile. Printati aria calculata a dreptunghilui
print("Exercitiul 15")

lungime = int(input("Lungime: "))
latime = int(input("Latime"))
print(int(lungime * latime))

print("----------------------------------------------")

# 16.citeste de la tastatura un string de dimensiune impara
# afiseaza caracterul din mijloc
print("Exercitiul 16")

random = input("Dimensiune impara :")
mijloc = random[len(random)//2]
print(mijloc)

print("----------------------------------------------")

# 17. folosind o singura linie de cod citeste un string de la tastatura (ex: 'alabala portocala')
# si salveaza fiecare cuvant intr-o variabila
# acum printeaza ambele variabile pentru verificare
print("Exercitiul 17")
ex1, ex2 = input("Scrie : ").split(" ")
print(f"  Prima   variabila : {ex1} ")
print(f"  A doua variabila : {ex2} ")


# x,y = "alabala" , "portocala"
# print(x,y)

print("----------------------------------------------")

# 18. citeste un string de la tastatura (eg: alabala portocala)
# salveaza primul caracter intr-o variabila (indiferent care este el, incearca cu 2 stringuri diferite)
# capitalizeaza acest caracter peste tot, mai putin pentru primul si ultimul caracter
# => alAbAlA portocAla
print("Exercitiul 18")

exemplu = input("Scrie ceva: ")
exemplu1 = exemplu[0]
print(exemplu[0] + exemplu[1:-1].replace(exemplu1 , exemplu1.capitalize()) + exemplu[-1])





print("----------------------------------------------")

# 19.citeste un user de la tastatura
# citeste o parola
# afiseaza: 'Parola pt user x este ***** si are x caractere'
# ***** se va calcula dinamic, indiferent de dimensiunea parolei, trebuie sa afiseze corect
# eg: parola abc => ***
# parola abcd => ****
print("Exercitiul 19")

user = input("User :")
parola = input("Parola :")
cod = len(parola)
caractere = "*" * len(parola)
parola = cod * caractere
print(f" Parola pentru  user {user} este  {caractere} si are {cod} caractere ")

print("----------------------------------------------")


