import math
#trojkat

a = 10
b = 12
c = 8
h = 6

pole_trojkata = 1/2 *a*h
obwod_trojkata = a+b+c
print("Pole trojkata wynosi: " + str(pole_trojkata) + ", a obwód wynosi " + str(obwod_trojkata))

# romb
a = 10
obwod_rombu = a*4
e=10
f=12
pole_rombu = (e*f)/2
print("Obwod rombu wynosi: " + str(obwod_rombu) + ", a pole wynosi " +str(pole_rombu))

#trapez
a = 15
b = 4
c = 3
d= 4
h = 6

pole_trapezu = ((a+b)*h)/2
obwod_trapezu = a+b+c+d
print("Obwod trapezu wynosi: " + str(obwod_trapezu) + ", a pole wynosi " +str(pole_trapezu))
#prostokat
a= 15
b = 4

pole_prostokata = a*b
obwod_prostokata = a*2+b*2
print("Obwod trapezu wynosi: " + str(obwod_prostokata) + ", a pole wynosi " +str(pole_prostokata))

#kolo
r = 10
obwod_kola = 2*math.pi*r
pole_kola = math.pi*math.pow(r,2)
print("Obwod kola wynosi: " + str(obwod_kola) + ", a pole wynosi " +str(pole_kola))