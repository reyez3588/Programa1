"""Esta clase contendrá figuras geométricas
para calcular sus respectivas áreas"""

class FiguraGeometrica:
    def __init__(self, area):
        self.__area = area

    def getterArea(self):
        return self.__area

class Circulo(FiguraGeometrica):
    _pi = 3.1416
    def __init__(self, radio: float):
        self.__radio = radio
        self.__area = self.__calcularArea()
        super().__init__(self.__area)

    def __calcularArea(self):
        return self._pi * (self.__radio * self.__radio)

    def setterRadio(self, nuevoRadio: float):
        self.__radio = nuevoRadio
        self.__area = self.__calcularArea()
        super().__init__(self.__area)


class Cuadrado(FiguraGeometrica):
    def __init__(self, lado: float):
        self.__lado = lado
        self.__area = self.__calcularArea()
        super().__init__(self.__area)

    def __calcularArea(self):
        return self.__lado * self.__lado

    def setterLado(self, nuevoLado: float):
        self.__lado = nuevoLado
        self.__area = self.__calcularArea()
        super().__init__(self.__area)


