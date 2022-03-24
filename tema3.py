# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 3 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Structuri de date din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 4 despre Flow Control din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# b. Usor spre Mediu (obligatoriu)
#
# 1. Declara o lista note_muzicale in care sa pui do re mi etc pana la do
# Afiseaz-o
# Inverseaza ordinea folosind slicing si suprascrie aceasta lista
# Printeaza varianta actuala (inversata)
# Pe aceasta lista, aplica o metoda care banuiesti ca face acelasi lucru, adica sa ii inverseze ordinea.
# (Nu trebuie sa o suprascrii in acest caz, deoarece metoda face asta automat)
# Printeaza varianta actuala a listei. Practic ai ajuns inapoi la varianta initiala
#
# Concluzii: slicing e temporar, daca vrei sa pastrezi noua varianta va trebuie sa suprascrii lista sau sa o salvezi
# intr-o lista noua. Metoda gasita de tine, face suprascrierea automat si permanentizeaza aceste modificari.
# Ambele variante isi gasesc utilitatea in functie de ce ne dorim in acel moment.

note_muzicale = ["do", "re", "mi", "fa", "so", "la", "si", "do"]
print(note_muzicale)
note_muzicale = note_muzicale[::-1]
print(note_muzicale)
note_muzicale.reverse()
print(note_muzicale)

# 2.  De cate ori apare ‘do’?
note_muzicale = str(note_muzicale)
print(note_muzicale.find("do"))
# 3 .Avand 2 liste, [3, 1, 0, 2] si [6, 5, 4]
# Gasiti 2 variante sa le uniti intr-o singura lista.
lista1 = [3, 1, 0, 2]
lista2 = [6, 5, 4]
varianta1 = lista1 + lista2
print(varianta1)
varianta2 = [*lista1, *lista2]
print(varianta2)
# 4. Sortati si afisati lista generata la ex anterior
# Stergeti numarul 0 folosind o functie
# Afisati iar lista
varianta1.sort()
print(varianta1)
varianta1.remove(0)
print(varianta1)
# 5.  Folosind un if verificati lista generata la ex3 si afisati
# Lista este goala
# Lista nu este goala
if len(varianta1) == 0:
    print("Lista este goala")
if len(varianta1) > 0:
    print("Lista nu este goala")
# 6. Folositi o functie care sa stearga lista de la ex3
varianta1.clear()
print(varianta1)
# 7. Copy paste la ex 5. Verificati inca o data.
# Acum ar trebui sa se afiseze ca lista e goala
if len(varianta1) == 0:
    print("Lista este goala")
if len(varianta1) > 0:
    print("Lista nu este goala")

# 8. Avand dictionarul dict1 = {'Ana' : 8, 'Gigel' : 10, 'Dorel' : 5}
# Folositi o functie ca sa afisati Elevii (cheile)
dict1 = {'Ana': 8, 'Gigel': 10, 'Dorel': 5}
print(dict1.keys())
# 9. Printati cei 3 elevi si notele lor
# Ex: ‘Ana a luat nota {x}’
# Doar nota o veti lua folosindu-va de cheie
print("Ana a luat nota", dict1["Ana"])
print("Gigel a luat nota", dict1["Gigel"])
print("Dorel a luat nota", dict1["Dorel"])
# 10. Dorel a facut contestatie si a primit 6
# Modificati nota lui Dorel in 6
# Printati nota dupa modificare
dict1["Dorel"] = 6
print(dict1["Dorel"])
# 11.Gigel se transfera din clasa
# Cautati o functie care sa il stearga
# Vine un coleg nou. Adaugati Ionica, cu nota 9
# Printati dictionarul schimbat
dict1.pop("Gigel")
dict1["Ionica"] = 9
print(dict1)
# 12.Set
# zile_sapt = {'luni', 'marti', 'miercuri', 'joi', 'vineri', 'sambata', 'duminica'}
# weekend = {'sambata', 'duminica'}
# Adaugati in zilele_sapt ‘luni’
# Afisati zile_sapt
zile_sapt = {"luni", "marti", "miercuri", "joi", "vineri", "sambata", "duminica"}
weekend = {"sambata", "duminica"}
zile_sapt.add("luni")
print(zile_sapt)
# 13 Folositi un if si verificati daca  Weekend este un subset al zilelor din sapt Weekend nu este un subset al zilelor din sapt
# 14 Afisati diferentele dintre aceste 2 seturi (exercitiu 12)
# 15 Afisati intersectia elementelor din aceste 2 seturi (exercitiu 12)
if zile_sapt.union(weekend) == zile_sapt:
    print("Weekend este un subset al zilelor saptamanii")
else:
    print(f"Nu este un subset deoarece exista diferenta de{zile_sapt.difference(weekend)} ")
    print(f"Nu este un subset deoarece exista diferenta de {zile_sapt.intersection(weekend)}")

# 16 Ne imaginam o echipa de fotbal pt teren sintetic.
# 3 Schimbari maxime admise
# Declara o Lista cu 5 jucatori
# Schimbari_efectuate = va jucati voi cu valori diferite
# Schimbari_max = 3
# Daca Jucatorul x e in teren si mai avem schimbari la dispozitie
# Efectuam schimbarea
# Stergem jucatorul scos din lista
# Adaugam jucatorul intrat
# Afisam a intra x, a iesit y, mai aveti z schimbari
# Daca jucatorul nu e in teren:
# Afisati ‘ nu se poate efectua schimbarea deoarece jucatorul x nu e in teren’
# Afisati ‘mai aveti z schimbari’
# Testati codul cu diferite valori
# Google search hint “how to check if item is in list python”


jucatori = ["Samy", "Alex", "Andrei", "Adi","Vlad"]
jucatori_schimbati = input("Il schimb pe : ").capitalize()
schimbari = 3

if jucatori_schimbati in jucatori and schimbari < 4:
    prima = input("Cu :").capitalize()
    jucatori.remove(jucatori_schimbati)
    jucatori.append(prima)
    schimbari = schimbari -1
    print(f"A intrat {prima} si a iesit {jucatori_schimbati} mai ai {schimbari} schimbari")
else:
    print(f"Nu se poate schimba deoarece {jucatori_schimbati} nu este in teren")
    print(f"mai aveti {schimbari} schimbari")
