"""En esta sesión se crearán clases y se instaciarán objetos

Clase: libros
Características Comunes: Hojas, espiral, tapa o pasta
Acciones Comunes: redactar(escribir), leer, informar
Objetos: libro, libreta, cuaderno

Atributos -> Características comunes
Métodos -> Las acciones que puede realizar un objeto perteneciente a una clase
"""

class Libros:
    def __init__(self, numHojas, espiral, tipoPasta):
        self.numHojas = numHojas
        self.espiral = espiral
        self.tipoPasta = tipoPasta

    def describir(self):
        print("El libro tiene", self.numHojas, "hojas")
        if self.espiral == True:
            print("El libro SI tiene espiral")
        else:
            print("El libro NO tiene espiral")
        print("El libro tiene pasta: " + self.tipoPasta)

    def escribir(self, numParrafos):
        print("Estoy escriendo ", numParrafos, "parrafos")

    def leer(self, numParrafos):
        print("Estoy leyendo", numParrafos, "parrafos")


cuaderno = Libros(500,False,"Dura")
cuaderno.leer(3)
cuaderno.escribir(60)
cuaderno.describir()










