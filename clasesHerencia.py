
"""En este archivo se encuentran las clases pertenecientes a los temas de herencia"""

#Superclase Persona
class Persona:
    def __init__(self, nombre, edad, estatura, peso, genero = "x"):
        self.__nombre = nombre
        self.genero = genero
        self.__edad = edad
        self.__estatura = estatura
        self.__peso = peso

    def describir(self):
        print(" ")
        print("Nombre:", self.__nombre)
        print("Género:", self.genero)
        print("Edad:", self.__edad)
        print("Estatura:", self.__estatura)
        print("Peso:", self.__peso)

    """
    def __setattr__(self, key, value):
        print(self.__dict__)
    """

    def setNombre(self, value):
        #print(self.__dict__)
        #self.__dict__["_Persona__" + key] = value
        self.__nombre = value
        #print("Setter...")

#Declaración de subclase
class Empleado(Persona):
    def __init__(self, nombre, edad, estatura, peso, sueldo, antiguedad, genero = "x"):
        super().__init__(nombre, edad, estatura, peso, genero)
        self.__sueldo = sueldo
        self.__antiguedad = antiguedad
        #print("Objeto de la clase empleado instanciado")

    def describir(self):
        super().describir()
        print("Sueldo:", self.__sueldo)
        print("Antigûedad:", self.__antiguedad)

#Declaración de la subclase estudiante
class Estudiante(Persona):
    def __init__(self, nivel, promedio, nombre, edad, estatura, peso, genero="x"):
        super().__init__(nombre, edad, estatura, peso, genero)
        self.__nivel = nivel
        self.__promedio = promedio

    def describir(self):
        super().describir()
        print("Nivel:", self.__nivel)
        print("Promedio: ", self.__promedio)



#Subclase de la clase Empleado
class Profesion(Empleado):
    def __init__(self, nombre, edad, estatura, peso, empleo, sueldo, antiguedad, genero = "x"):
        super().__init__(nombre, edad, estatura, peso, sueldo, antiguedad, genero)
        self.__empleo = empleo

    def describir(self):
        super().describir()
        print("Profesión:", self.__empleo)
