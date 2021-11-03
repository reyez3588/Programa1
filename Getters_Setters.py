"""ENCAPSULAMIENTO
PASOS:
1.-DEFINIR UN CLASE (Abstracción)
2.- INSTANCIAR UN OBJETO
3.- realizar programa que utilice las clases creadas
"""

class Computadora:
    #método constructor
    def __init__(self, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla, costo, tarjetaVideo = "Integrada", tipoSO = None):

        if str(type(memRAM)) == "<class 'int'>":
            self.__memRAM = memRAM
        else:
            print("el valor de RAM debe ser un numero entero")
            self.__del__()
            return
        self.__tipoProcesador = tipoProcesador
        self.__capAlmacenamiento = capAlmacenamiento
        self.__tarjetaVideo = tarjetaVideo
        self.__tamañoPantalla = tamañoPantalla
        self.__tipoSO = tipoSO
        self.costo = costo
        print("Objeto de la clase computadora instanciado")


    #Método destructor
    def __del__(self):
        print("objeto destruido")

    #Métodos de la clase
    def ejecutarProcesos(self, numProcesos):
        print("Ejecutando", numProcesos, "procesos")

    def reproducirVideo(self, nombreVideo):
        print("Reproduciendo video", nombreVideo)

    #Método encapsulado
    def __mostrarInfo(self):
        print("El objeto tiene las siguientes características")
        print("El tipo de procesador es: ", self.__tipoProcesador)
        print("La memoria ram es de: ", self.__memRAM)
        print("La capacidad de almacenamiento es: ", self.__capAlmacenamiento)
        print("La tarjeta de video es: ", self.__tarjetaVideo)
        print("El tamaño de pantalla es: ", self.__tamañoPantalla)
        print("El sistema operativo es: ", self.__tipoSO)
        print("El costo es: ", self.costo)
        print("  ")

    #Declaración de Getters
    def getterInfo(self):
        self.__mostrarInfo()
    def getterRAM(self):
        return  self.__memRAM

    #Declarar método Setter
    def setterRAM(self, newRAM):
        self.__memRAM = newRAM

    def __setattr__(self, key, value):
        self.__dict__[key] = value

    #Sobrecarga de operaciones
    def __add__(self, *other):
        suma = self.__memRAM
        for arg in other:
            suma = suma + arg.__memRAM
        return  suma

    def __sub__(self, other):
        print(self.__memRAM - other.__memRAM)





