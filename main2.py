"""PROGRAMA PRINCIPAL
desde este programa se accesará a la clase creada"""

import csv
import claseAlumnos as cAlumnos
#Leer como diccionario

listAlumnos = []

with open('calificaciones.csv') as csvfile:
    misCalificaciones = csv.DictReader(csvfile)

    for filas in misCalificaciones:
        auxAlumno = cAlumnos.Alumno(filas['Nombre'], float(filas['Unidad 1']), float(filas['Unidad 2']),
                                    float(filas['Unidad 3']), float(filas['Unidad 4']))
        listAlumnos.append(auxAlumno)
    csvfile.close()

for alumno in listAlumnos:
    print("Nombre:", alumno.getNombre() + ",", "Promedio:", alumno.getPromedio())

print("Se supone que esto debe estar en linea")