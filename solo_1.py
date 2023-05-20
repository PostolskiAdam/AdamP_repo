#Zadanie 1.1
hello = "Hello"
student = "Adam"
print( "{} {}".format(hello, student) )

#Zadanie 1.2
student = input("Wpisz swoje imie: ")
print("hello " + student)

#Zadanie 1.3
studenci = ["Ania", "Kuba", "Piotr", "Jan"]
liczba_studentow = len(studenci)
print(liczba_studentow)


#zadanie 1.4
for student in studenci:
    print("Hello " + student)


#Zadanie 1.5
liczba = 3
potega = 4
wynik = pow(liczba, potega)
print(wynik)

#zadanie 1.6
ciag_znakow = "edbw(hdakqas(skqskahb))adwndwb(wgwidn()dsqwhjdw)"
liczba_nawiasow_otwierajacych = ciag_znakow.count('(')
print("Liczba nawiasow otwierajacych wynosi: " + str(liczba_nawiasow_otwierajacych))

#zadanie 1.7
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
studenci.sort()
for student in studenci:
    print(student)

#zadanie 1.8

studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
nazwiska = []

for student in studenci:
    last_name = student.split(" ")
    nazwiska.append(last_name[1])

print(nazwiska)



#zadanie 1.9
studenci = ["Anna Szczesny", "Tomasz Nijaki", "Barbara Kowalska", "Jan Niezbedny"]
nazwiska = []
liczba_n = 0
for student in studenci:
    last_name = student.split(" ")
    nazwiska.append(last_name[1])
for nazwisko in nazwiska:
    if nazwisko[0] == "N":
        liczba_n += 1
print("Liczba studentów na N wynosi " + str(liczba_n))



# zadanie 1.10


wykres_1 = [[2, 4], [4, 4], [6, 4]]
wykres_2 = [[2, 3], [4, 4], [6, 5]]
wykres_3 = [[2, 3], [4, 3], [5, 4]]


wykres_1_funkcja_liniowa = False
wykres_2_funkcja_liniowa = False
wykres_3_funkcja_liniowa = True

if wykres_1_funkcja_liniowa:
    print("Dla punktow w wykres_1 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_1 nie mozna wyznaczyc funkcji liniowej.")

if wykres_2_funkcja_liniowa:
    print("Dla punktow w wykres_2 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_2 nie mozna wyznaczyc funkcji liniowej.")

if wykres_3_funkcja_liniowa:
    print("Dla punktow w wykres_3 mozna wyznaczyc funkcje liniowa.")
else:
    print("Dla punktow w wykres_3 nie mozna wyznaczyc funkcji liniowej.")
