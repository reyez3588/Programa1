
#En este programa realizaremos comandos básicos de python

'''Este es un comentario multilinea
por lo que puedo escribir varias lineas
y  sera omitido por el interprete
aca puedo seguir y sigue siendo parte del mismo comentario'''

#Declaración de variables
a = 10
b = 6.3
varStr = "Pedro"
c = 'Jose'

#imprimir variables
print("La variable a = %i \r\nLa variable b = %f" %(a,b))
print("La variable a =", a)
print("La variable b =", b)
print("Hola",varStr)
print("hola " + varStr)
print (varStr + c)
print("\r\n")
print("\r\n")
print("\r\n")

'''Variables propias de Python:
Lista [], almacena datos que son de diferente tipo, perimite cambiar o actualizar sus elementos
Tupla ()
Diccionario {}
'''

myList = [5, "Charly", 13.5, "Abel"]
print(type(myList))
myList[1] = varStr
print(myList)
myList.append("poner esto al final")
print(myList)

print("\r\n")
print("\r\n")

#Variable Tupla
myTuple = ("Anahi", 170, "Manuel", 185.2)
print(myTuple[1])
print("\r\n")
print("\r\n")

#Variable Diccionario, item, key, value
myDic = {"Juan" : 19, "Ricardo" : 21, "Fabian" : 20}
print(myDic.items())
#print(myDic.get("Fabian"))
#print(myDic.keys())
#print(myDic.values())
myDic["Ricardo"] = 30
print(myDic.items())

for key in myDic:
    print(key,":", myDic[key])

print("\r\n")

myDic.update({"Lola":30, "Jesus":3})
for key in myDic:
    print(key,":", myDic[key])

