"""PROGRAMA PRINCIPAL
desde este programa se accesará a la clase creada"""

import pointClass

#p3 a p4 son los puntos que tienen la menor distancia e imprimir la distancia entre ellos
p1 = pointClass.Punto(1,1)
p2 = pointClass.Punto(0,10)
p3 = pointClass.Punto(-8,4)
p4 = pointClass.Punto(1,3)
listaPuntos = [p1, p2, p3, p4]

distancia = []
cont = 0
minPar = [cont, 0]
for point in listaPuntos:
    for i in range(len(listaPuntos)):
        if cont == i:
            continue

        distancia.append(point.calDist(listaPuntos[i]))

        if distancia[-1] <= min(distancia):
            minDist = distancia[-1]
            minPar = [cont, i]
        #print(distancia)
    cont = cont + 1

"""
Valores utilizados:
p1 = pointClass.Punto(1,1)
p2 = pointClass.Punto(0,10)
p3 = pointClass.Punto(-8,4)
p4 = pointClass.Punto(1,3)
listaPuntos = [p1, p2, p3, p4]
"""
print("El primer punto tiene las coordenadas:")
listaPuntos[minPar[0]].printPoint()
print("El segundo punto tiene las coordenadas:")
listaPuntos[minPar[1]].printPoint()
print("La distancia entre estos puntos es:", minDist)






