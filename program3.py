'''En este programa se verá sintaxis para if, for y while'''
import myFuncts
import numpy as np

'''
a = int(input("Ingresar la variable a "))
b = int(input("Ingresar la variable b "))

c = a + b
#print(c)

if a == b:
    if a != 0:
        print("a es diferente de cero")
    print("Los números son iguales")
else:
    print("Los números son diferentes")


#varX = int(input("Ingrese el numero a iterar"))

myList = [5, "Charly", 13.5, "Abel"]
for x in myList:
    #print(x)
    if x == 13.5:
        #print("Salir del ciclo for")
        break

while True:
    a = int(input("Ingresar la variable a "))
    b = int(input("Ingresar la variable b "))
    if a != b:
        print("Los números son diferentes")
        break
print("El ciclo while ha terminado")


'''
import myFuncts as mF

x  = np.arange(5)
print(x)

a = int(input("Ingresar la variable a "))
b = int(input("Ingresar la variable b "))

suma = mF.sumXY(a,b)
print(suma)
times = mF.multXY(a,b)
print(times)