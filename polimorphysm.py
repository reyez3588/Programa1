"""
UNIDAD 4: POLIMORFISMO
"""

class Animal:
    def __init__(self):
        pass

    def emitirSonido(self):
        print(type(self).__name__, "emitiendo sonido")

class Mascota(Animal):
    def __init__(self):
        pass

class Perro(Mascota):
    def __init__(self):
        pass

    def emitirSonido(self, cantLadridos = 1): #Esto si es polimorfismo
        print("guau!!! " * cantLadridos)

class Gato(Mascota):
    def __init__(self):
        pass

    def emitirSonido(self): # esto también es polimorfismo
        print("Miau, miau!!!")

class Vaca(Animal):
    def __init__(self):
        pass

    def emitirSonido(self): # esto también es polimorfismo
        print("Muuuuuuuuuuuuuuuuuuuuuuuuuuu !!!")







