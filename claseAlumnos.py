"""
En esta clase se utilzará información de un arvhivo csv
"""

class Alumno:
    def __init__(self, nombre, calU1, calU2, calU3, calU4):
        self.__nombre = nombre
        self.__calU1 = calU1
        self.__calU2 = calU2
        self.__calU3 = calU3
        self.__calU4 = calU4
        self.__promedio = self.__calPromedio()


    def getNombre(self):
        return self.__nombre
    def getPromedio(self):
        return self.__promedio

    def __calPromedio(self):
        prom = (self.__calU1 + self.__calU2 + self.__calU3 + self.__calU4)/4
        return prom
