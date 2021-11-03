"""En este archivo tendremos la clase vehículo a la cual le aplicaremos herencia múltiple"""

class VehiculoElectrico:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.capBateria = None
        self.yearProduction = None
        self.potencia = None
        self.precio = None
        self.carga = False

    def cargar(self, condicion = True):
        if condicion:
            self.carga = True
        else:
            self.carga = False

    def describir(self):
        print(" ")
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Año de producción:", self.yearProduction)
        print("Potencia:", self.potencia)
        print("Precio:", self.precio)
        if self.carga:
            print("Cargando vehículo...")

    def setModelo(self, nuevoModelo):
        self.__modelo = nuevoModelo
        print("setter de clase VehiculoElectrico")


class Vehiculo:
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
        self.tipoMotor = None
        self.yearProduction = None
        self.potencia = None
        self.precio = None
        self.nivelEquipamiento = None
        self.tipoCombustible = None


    def getMarca(self):
        return  self.__marca
    def getModelo(self):
        return self.__modelo

    def setMarca(self, nuevaMarca):
        self.__marca = nuevaMarca
    def setModelo(self, nuevoModelo):
        self.__modelo = nuevoModelo
        print("setter de clase Vehiculo")

    def describir(self):
        print(" ")
        print("Marca:", self.__marca)
        print("Modelo:", self.__modelo)
        print("Tipo de motor:", self.tipoMotor)
        print("Año de producción:", self.yearProduction)
        print("Potencia:", self.potencia)
        print("Precio:", self.precio)
        print("Tipo de combustible:", self.tipoCombustible)
        print("Nivel de equipamiento:", self.nivelEquipamiento)

    def avanzar(self):
        print(type(self).__name__, "esta avanzando...")

class motocicleta(Vehiculo):
    def __init__(self, marca, modelo, tipoEncendido, dimensiones = None):
        super().__init__(marca, modelo)
        self.tipoEncendido = tipoEncendido
        self.dimenciones = dimensiones
        self.caballito = False

    def hacerCaballito(self, condicion = True):
        if condicion:
            self.caballito = True
        else:
            self.caballito = False

    def describir(self):
        super().describir()
        if self.caballito:
           print(type(self).__name__, "haciendo caballito...")


class Automovil(VehiculoElectrico, Vehiculo):
    def __init__(self, marca, modelo, hibrido = False):
        self.hibrido = hibrido
        #Vehiculo.__init__(self, marca, modelo) #correr el constructor de la clase Vehiculo
        super(Automovil, self).__init__(marca, modelo)
        if self.hibrido:
            VehiculoElectrico.__init__(self, marca, modelo)
        self.cantPuertas = None
        self.numAsientos = None

    def describir(self):
        if self.hibrido:
            VehiculoElectrico.describir(self)
        else:
            Vehiculo.describir(self)
        print("Cantidad de puertas", self.cantPuertas)
        print("Número de asientos", self.numAsientos)



