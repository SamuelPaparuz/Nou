import math
from calendar import monthrange
import datetime
from datetime import date

print("Exercitiul 1")
# 1. Functie care sa calculeze si sa returneze suma a 2 numere


def suma(x,y):
    suma = x + y
    return suma


print(f"Suma celor doua nr este : {suma(1,6)}")

print("-----------------------------------------")
print("Exercitiul 2")
# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

def nr(par):
    if par % 2 == 0:
        return True
    else:
        return False
print(nr(24))

print("-----------------------------------------")
print("Exercitiul 3")
# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)


def persoana(nume, prenume,nume_mijlociu):
    persoana = len(nume) + len(prenume)+len(nume_mijlociu)
    return persoana
print(persoana("samy","paparuz","nimic"))
print("-----------------------------------------")
print("Exercitiul 4")
# 4. Functie care returneaza aria dreptunghiului


def aria(lungime , latime):
    aria = lungime * latime
    return aria


print(aria(2,3))

print("-----------------------------------------")
print("Exercitiul 5")
# 5. Functie care returneaza aria cercului


def cerc(r):
    if r > 0:
        arie = math.pi*r*r
        return arie
    else:
        return "introdu o valoare valida"


print(cerc(1))

print("-----------------------------------------")
print("Exercitiul 6")
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu !


def caracter(caracterul, cuvant ):
    for x in range(len(cuvant)):
        if cuvant[x] == caracterul:
            return True
        else:
            return False


print(caracter("b", "samy"))

print("-----------------------------------------")
print("Exercitiul 7")
# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case este y

def caract(ecran):
    c_mici = 0
    c_mari = 0
    for a in ecran:
        if a.isupper() == True:
            c_mari += 1
        elif a.islower() == True:
            c_mici += 1
    print(f"caractere lower {c_mici} , caractere upper{c_mari}")
print(caract("Paparuz Samuel"))
print("-----------------------------------------")
print("Exercitiul 8")
# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive


def pozitive(nr):
    poz = []
    for a in nr:
        if a >= 0:
            poz.append(a)
    return poz


print(pozitive([-22, 33, 55, -1]))

print("-----------------------------------------")
print("Exercitiul 9")
# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.


def verificare(x,y):
    if x > y:
        print(f"Primul numar {x} este mai mare decat al doilea nr {y}")
    elif x <y:
        print(f"Al doilea nr {y} este mai mare decat primul nr {x}")
    else:
        print(f"Numarul {x} si {y} sunt egale")
verificare(2,2)

print("-----------------------------------------")
print("Exercitiul 10")
# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False


def set(nr,set_nr):
    if nr in set_nr:
        print("nu am adaugat numarul in set. Acesta exista deja")
        return False
    else:
        print("am adaugat numarul nou in set")
        return True


set(9,[1,2,3,4,5,6])

print("-----------------------------------------")
print("Exercitiul 11")
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna


def nr_zile(year, month):
    return monthrange(year, month)[1]

print(nr_zile(2022,3))

print("-----------------------------------------")
print("Exercitiul 12")
#12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)


def adunare(x,y):
    nr = x+y
    return nr


def scadere(x,y):
    nr = x-y
    return nr


def inmultire(x,y):
    nr = x * y
    return nr


def impartire(x,y):
    nr = x / y
    return nr


def calculator(x,y):
    print("Adunare : ", adunare(x,y))
    print("Scadere : ", scadere(x,y))
    print("inmultire : ",inmultire(x,y))
    print("Impartire : ",impartire(x,y))
calculator(2,2)

print("-----------------------------------------")
print("Exercitiul 13")
# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare litera
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }
# lista = [1, 3, 1, 5, 9, 7, 7, 5, 5]
#
def numarat(lista : list):
    dict1 = {}
    for i in range(len(lista) + 1):
            dict1[i] = lista.count(i)
    return dict1
print(numarat([1,2,3,4,5,1]))

print("-----------------------------------------")
print("Exercitiul 14")
# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele


def valoare_maxima(x,y,z):
    return max(x,y,z)


print(valoare_maxima(10,12,33))




print("-----------------------------------------")
print("Exercitiul 15")
# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3


def numar_adunat(n):

    suma = n * (n + 1) / 2
    return suma


print(numar_adunat(7))


print("-----------------------------------------")
print("Exercitiul 16")
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’


def nume_romanesti(nume):
    nume =nume

    baieti = ['Adam', 'Adelin', 'Adrian','Alex','Alexandru','Alexie','Alin','Amos','Andreas','Andrei','Anghel','Anton','Apostol','Arsenie','Barbu','Bartolomeu','Basarab','Benedict','Benone','Bogdan','Boris','Bujor','Calin','Camil','Cazimir','Cezar','Ciprian','Codrut','Constantin','Cornel','Cosmin','Costel','Costin','Craciun','Cristi','Cristian','Cristofor','Damian','Dan','Daniel','David','Decebal','Denis','Dimitrie','Dionisie','Dorin','Doru','Dragos','Dumitru','Eduard','Efrem','Emil','Emilian','Eugen','Eusebiu','Fabian','Fanurie','Felix','Filip','Florian','Gabriel','Gelu','George','Gheorghe','Ghita','Grig','Grigore','Haralambie','Horia','Iacob','Ilarie','Ilie','Ioachim','Ioan','Ion','Ionut','Iosif','Iurie','Iustin','Laur','Laurentiu','Lazar','Leon','Liviu','Luca','Luchian','Lucian','Lucretiu','Madalin','Manole','Manuel','Marian','Marin','Martin','Matei','Mihai','Mihail','Narcis','Nectarie','Neculai','Nicolae','Nicolai','Norbert','Oscar','Paul','Pavel','Petre','Petru','Razvan','Sebastian','Sorin','Spiridon','Stefan','Stelian','Teodor','Teodosie','Toma','Valentin','Valeriu','Vasile','Vitalie','Vladimir','Zaharia']

    fete = list1='''Ada,Adela,Adelaida,Adelina,Adina,Adriana,Adnana,Agata,Aglaia,Agripina,Aida,Alberta,Albertina,Alexandra,Alexandrina,Alexia,Alice,Alida,Alina,Alis,Alma,Amalia,Amanda,Amelia,Ana,Anabela,Anaida,Anamaria,Anastasia,Anca,Ancuța,Anda,Andra,Andrada,Andreea,Anemona,Aneta,Angela,Angelica,Anghelina,Anica,Anișoara,Antoaneta,Antonela,Antonia,Anuța,Ariadna,Ariana,Arina,Aristița,Artemisa,Astrid,Atena,Augusta,Augustina,Aura,Aurelia,Aureliana,Aurica,Aurora,Axenia,Beatrice,Betina,Bianca,Blanduzia,Bogdana,Brândușa,Camelia,Carina,Carla,Carmen,Carmina,Carol,Carolina,Casandra,Casiana,Caterina,Catinca,Catrina,Catrinel,Cătălina,Cecilia,Celia,Cerasela,Cezara,Chira,Cipriana,Clara,Clarisa,Claudia,Clementina,Cleopatra,Codrina,Codruța,Constanța,Constantina,Consuela,Coralia,Corina,Cornelia,Cosmina,Crenguța,Crina,Cristina,Daciana,Dafina,Daiana,Dalia,Dana,Daniela,Daria,Dariana,Delia,Demetra,Denisa,Despina,Diana,Dida,Didina,Dimitrina,Dina,Dochia,Doina,Domnica,Dora,Doriana,Dorina,Dorli,Draga,Dumbrăvița,Dumitra,Dumitrana,Ecaterina,Eftimia,Elena,Eleonora,Eliana,Elisabeta,Elisaveta,Eliza,Elodia,Elvira,Emanuela,Emilia,Erica,Estera,Eufrosina,Eugenia,Eusebia,Eva,Evanghelina,Evelina,Fabia,Fabiana,Felicia,Fausta,Filofteia,Filomela,Fiona,Flavia,Floare,Floarea,Flora,Florența,Florentina,Floriana,Florica,Florina,Francesca,Frusina,Gabriela,Geanina,Gențiana,Georgeta,Georgia,Georgiana,Geta,Gherghina,Gianina,Gina,Giorgiana,Gloria,Glorița,Grațiana,Grațiela,Henrieta,Heracleea,Hortensia,Iasmina,Ica,Ilaria,Ileana,Ilinca,Ilona,Ina,Ioana,Ioanina,Iolanda,Ionela,Ionelia,Ionuța,Iosefina,Iridenta,Irina,Iris,Irma,Isabela,Isaura,Iulia,Iuliana,Iustina,Ivana,Ivona,Izabela,Izaura,Jana,Janeta,Janina,Jasmina,Jeana,Joița,Julia,Julieta,Larisa,Laura,Laurenția,Lavinia,Lăcrămioara,Leana,Lelia,Leontina,Leopoldina,Letiția,Lenuța,Lia,Liana,Lidia,Lidia,Ligia,Lili,Liliana,Lioara,Livia,Loredana,Lorelei,Lorena,Luana,Lucia,Luciana,Lucreția,Ludmila,Ludovica,Luiza,Luminița,Magdalena,Maia,Malvina,Manuela,Mara,Marcela,Marcheta,Marga,Margareta,Maria,Mariana,Maricica,Marieta,Marilena,Marina,Marinela,Marioara,Marta,Martina,Marusia,Matilda,Mădălina,Mălina,Mărioara,Măriuca,Melania,Melina,Melinda,Melisa,Mia,Mihaela,Milena,Minodora,Mioara,Mirabela,Miranda,Mirela,Mirona,Miuța,Miruna,Mona,Monalisa,Monica,Nadia,Naomi,Narcisa,Natalia,Natașa,Nicoleta,Niculina,Nidia,Nina,Noemi,Nora,Norica,Oana,Octavia,Octaviana,Ofelia,Olga,Olimpia,Olivia,Ortansa,Otilia,Ozana,Pamela,Paraschiva,Patricia,Paula,Paulica,Paulina,Petria,Petrina,Petronela,Petruța,Pompilia,Profira,Rada,Rafila,Raluca,Ramona,Rebeca,Reghina,Renata,Rica,Rita,Roberta,Robertina,Rodica,Romana,Romanița,Romina,Roxana,Roxelana,Roza,Rozalia,Ruxanda,Ruxandra,Sabina,Sabrina,Safina,Safta,Salomea,Sanda,Sandra,Saveta,Savina,Săndica,Sânziana,Selina,Semenica,Smeralda,Serafina,Severina,Sidonia,Silvana,Silvia,Silviana,Simina,Simona,Smaranda,Sodica,Sofia,Sofica,Sonia,Sorana,Sorina,Speranța,Stana,Stanca,Stela,Steliana,Steluța,Susana,Suzana,Svetlana,Ștefana,Ștefania,Tamara,Tania,Tatiana,Teea,Teodora,Teodosia,Teona,Teresa,Tereza,Tiberia,Timea,Tinca,Tincuța,Tudora,Tudorica,Tudorița,Tudosia,Valentina,Valeria,Vanesa,Varvara,Vasilica,Vasilichia,Venera,ra,Veronica,Veta,Vicenția,Victoria,Violeta,Viorela,Viorica,Virginia,Viviana,Vlădelina,Voichița,Xenia,Zaharia,Zamfira,Zaraza,Zenaida,Zenobia,Zenovia,Zina,Zita,Zoe,'''.split(',')
    if nume in baieti:
        return 'Numele este de baiat'
    elif nume in fete:
        return "Numele este de fata"
    else:
        return "nu e nume romanesc"


print(nume_romanesti("Adam"))

print("-----------------------------------------")
print("Exercitiul 17")

# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}

def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
print(common_elements([1, 1, 2, 3],[2, 2, 3, 4]))

print("-----------------------------------------")
print("Exercitiul 18")
# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida

def magazin(produs,reducere):
    if reducere <= 100:
        rezultat = produs - (produs * reducere / 100)
        return rezultat
    else:
        return "nu ai cum sa ai o reducere mai mare decat 100%"


print(magazin(266,5))

print("-----------------------------------------")
print("Exercitiul 19")
# 19. Functie care sa afiseze data si ora curenta

def ora_data():
    timpul = datetime.datetime.now()
    return timpul
print(ora_data())

print("-----------------------------------------")
print("Exercitiul 20")
# 20 Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)


def nr_inversa(year , month, day):
    acum = date.today()
    zi_nastere = date(year, month, day)
    diferenta = zi_nastere - acum
    return diferenta




print(nr_inversa(2022,4,28))


print("-----------------------------------------")