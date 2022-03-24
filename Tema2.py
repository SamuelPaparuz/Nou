# 1.Explica cu cuvintele tale in cadrul unui comentari cum functioneaza un if else:

# If este o conditie ca ruleaza doar daca e adevarata , in momentul in care conditia este falsa va lua
# pe rand elif (daca exista) si daca si elif este false va lua else care automat va fi true
# 2. Verifica si afiseaza daca x este numar pozitiv sau nu
nr = int(input("Introdu nr: "))
if nr > 0:
    print(f"{nr} este numar pozitiv")
elif nr == 0:
    print(f"{nr} este numar null")
else:
    print(f"{nr} este numar negativ")

# 3.Verifica si afiseaza daca x este numar pozitiv, negativ sau neutru
# A fost adaugat in ex 2 elif nr == 0:
#     print("Numar null")

# 4. Verifica si afiseaza daca x este intre -2 si 13
if nr >= -2 and nr <=13:
    print("Numarul se afla intre -2 si 13")

# 5. Verifica si afiseaza daca diferenta dintre x si y este mai mica de 5
x = int(input("X: "))
y = int(input("Y: "))
if x-y < 5:
    print("Diferenta numerelor este mai mica de 5")
# 6. Verifica daca x NU este intre 5 si 27. (a se folosi ‘not’)
if not x>=5 and not x<=27:
    print("x Nu este intre 5 si 27")
# 7. x si y (int) Verifica si afiseaza daca sunt egale, daca nu afiseaza care din ele este mai mare
if x == y:
    print("Numerele sunt egale")
elif x>y:
    print(f"{x} este mai mare decat {y}")
else:
    print(f"{y} este mai mare decat {x}")
# 8.  X, y, z - laturile unui triunghi Afiseaza daca triunghiul este isoscel, echilateral sau oarecare.
x = int(input("Latura 1 :"))
y = int(input("Latura 2 :"))
z = int(input("Latura 3 :"))
if x == y and y == z:
    print("Acesta este un triunghi echilateral")
elif x == y or x == z or y == z:
    print("Acesta este un triunghi isoscel")
else:
    print("Acesta este un triunghi oarecare")
# 9. Citeste o litera de la tastatura Verifica si afiseaza daca este vocala sau nu
litera = (input("Introdu o litera : "))

if litera == "a" or litera =="e" or litera =="i" or litera =="o" or litera =="u":
    print(f"{litera} este o vocala")
else:
    print(f"{litera} este o consoana")


# 10.Transforma si printeaza notele din sistem românesc in sistem american dupa cum urmeaza
# Peste 9 => A ,Peste 8 => B ,Peste 7 => C, Peste 6 => D, Peste 4 => E ,4 sau sub => F

nota = float(input("Nota ta este : "))
if nota > 10 or nota < 1:
    print("Nota incorecta")
elif nota > 9:
    print("A")
elif nota > 8:
    print("B")
elif nota > 7:
    print("C")
elif nota > 6:
    print("D")
elif nota > 4:
    print("E")
elif nota < 4:
    print("F")

# 11.Verifica daca x are minim 4 cifre
# (ex: 7895 are 4 cifre, 10 nu are minim 4 cifre)

nr = int(input("Numar: "))

if len(str(nr)) < 4:
    print(f"{nr} nu are minim 4 cifre")
elif len(str(nr)) == 4:
    print(f"{nr} are 4 cifre")
elif len(str(nr)) == 6:       # 12.Verifica daca x are exact 6 cifre
    print(f"{nr} are 6 cifre")

# 13 Verifica daca x este numar par sau impar
if nr % 2 == 1 :
    print(f"{nr} este un nr impar")
else:
    print(f"{nr} este un nr par ")

# 14. x, y, z (int) Afiseaza care este cel mai mare dintre ele?
x = int(input("x: "))
y = int(input("y: "))
z = int(input("z: "))

if x > y and x > z:
    print(f"{x} este mai mare decat {y} si {z}")
elif y > x and y > z:
    print(f"{y} este mai mare decat {x} si {z}")
elif z > x and z > y:
    print(f"{z} este mai mare decat {x} si {y}")
elif x==y and x==z and y==z:
    print(f"{x} este egal cu {y} si {z}")
elif x == y and y > z:
    print(f"{x} si {y} sunt egale si sunt mai mari decat  {z}")
elif x ==z and z > y:
    print(f"{x} si {z} sunt egale si sunt mai mari decat {y}")
elif y == z and z > x:
    print(f"{y} si {z} sunt egale si sunt mai mari decat {x}")

# 15. X, y, z - reprezinta unghiurile unui triunghi
# Verifica si afiseaza daca triunghiul este valid sau nu
x = int(input("X :"))
y = int(input("Y :"))
z = int(input("Z :"))


if x <= 0 or y <= 0 or z <= 0:
    print("Triunghiul este invalid")
elif x + y + z == 180:
    print("Triunghiul este valid")
else:
    print("Triunghiul este invalid")