"""En este archivo se encontrarán las clases para la tienda Mercado Libre"""


#Declarar Super Clase
class Producto:
    def __init__(self, categoria, precio, titulo):
        self.__categoria = categoria
        self.__precio = precio
        self.__titulo = titulo

    #Declarar Getters y setters
    def getCategoria(self):
        return self.__categoria
    def getPrecio(self):
        return self.__precio
    def getTitulo(self):
        return self.__titulo

    def setPrecio(self, nuevoPrecio):
        self.__precio = nuevoPrecio
    def setTitulo(self, nuevoTitulo):
        self.__titulo = nuevoTitulo

    def __del__(self):
        print("El objeto de la clase:", type(self).__name__, "fue destruido")

#Declara la clase Teléfono
class Telefono(Producto):
    _categoria = "Telefono"
    def __init__(self, marca, modelo, precio, titulo):
        super().__init__(self._categoria, precio, titulo)
        self.__marca = marca
        self.__modelo = modelo

    def __describir(self):
        print("\n", super().getTitulo())
        print("Precio:", super().getPrecio())
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo )

    #Getters
    def getInfo(self):
        self.__describir()

    def getMarca(self):
        return self.__marca

    def getModelo(self):
        return self.__modelo

    #Setters
    def setMarca(self, nuevaMarca):
        self.__marca = nuevaMarca
    def setModelo(self, nuevoModelo):
        self.__modelo = nuevoModelo

#Subclase Celulares
class Celular(Telefono):
    _categoria = "Celular"
    def __init__(self, memInterna: int, memRAM, tipoSO, marca,
                 modelo, precio: str, titulo, tamanoPantalla = None):
        super().__init__(marca, modelo, precio, titulo)
        self.__memInterna = memInterna
        self.__memRAM = memRAM
        self.__tipoSO = tipoSO
        self.__tamanoPantalla = tamanoPantalla
        print(type(self.getPrecio()))

    def getInfo(self):
        super().getInfo()
        print("Memoria interna:", self.__memInterna)
        print("Memoria RAM:", self.__memRAM)
        print("Tipo de sistema operativo:", self.__tipoSO)
        if self.__tamanoPantalla != None:
            print("Tamaño de pantalla:", self.__tamanoPantalla)


########################################################################################################################
class Computadora(Producto):
    _categoria = "Computadora"

    #método constructor
    def __init__(self, titulo, precio, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla, tarjetaVideo = "Integrada", tipoSO = None):
        super().__init__(self._categoria, precio, titulo)
        self.__tipoProcesador = tipoProcesador
        self.__memRAM = memRAM
        self.__capAlmacenamiento = capAlmacenamiento
        self.__tarjetaVideo = tarjetaVideo
        self.__tamañoPantalla = tamañoPantalla
        self.__tipoSO = tipoSO

    #Método encapsulado
    def __mostrarInfo(self):
        print("\n", super().getTitulo())
        print("El Precio es:", super().getPrecio())
        print("El tipo de procesador es: ", self.__tipoProcesador)
        print("La memoria ram es de: ", self.__memRAM)
        print("La capacidad de almacenamiento es: ", self.__capAlmacenamiento)
        print("La tarjeta de video es: ", self.__tarjetaVideo)
        print("El tamaño de pantalla es: ", self.__tamañoPantalla)
        print("El sistema operativo es: ", self.__tipoSO)

    #Declaración de Getters
    def getInfo(self):
        self.__mostrarInfo()


class Laptop(Computadora):
    _categoria = "Laptop"
    def __init__(self, titulo, precio, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla,
                 tarjetaVideo = "Integrada", tipoSO = None, hAutonomia = None ):
        super().__init__(titulo, precio, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla, tarjetaVideo, tipoSO )
        #self.__categoria = self._categoria
        self.__hAutonomia = hAutonomia

    def getInfo(self):
        super().getInfo()
        print("Horas de autonomia:", self.__hAutonomia)

class miniLaptop(Laptop):
    _categoria = "Minilaptop"
    def __init__(self, titulo, precio, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla,
                 tarjetaVideo = "Integrada", tipoSO = None, hAutonomia = None, peso = None ):
        super().__init__(titulo, precio, tipoProcesador, memRAM, capAlmacenamiento, tamañoPantalla, tarjetaVideo, tipoSO, hAutonomia )
        self.__peso = peso

    def getInfo(self):
        super().getInfo()
        print("Peso:", self.__peso)


