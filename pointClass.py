#Crear la clase Punto
class Punto:
    def __init__(self, x = 0, y = 0):
        """
        Método constructor de la clase punto
        Comprueba si los parámetros son de tipo int o float para crear el objeto
        Si se instancia sin parámetros p1 = Punto() se crea un punto en el origen (0,0)
        :param x: coordenada x del punto
        :param y: coodenada y del punto
        """
        if str(type(x)) == "<class 'int'>" or str(type(x)) == "<class 'float'>":
            if str(type(y)) == "<class 'int'>" or str(type(y)) == "<class 'float'>":
                self.__x = x
                self.__y = y
                # print("Objeto punto instanciado, con coordenas: (", self.x, ",", self.y, ")")
            else:
                print("Solo se admiten datos de tipo int y float para crear el objeto de la clase punto")
                self.__del__()
        else:
            print("Solo se admiten datos de tipo int y float para crear el objeto de la clase punto")
            self.__del__()

    #Método destructor
    def __del__(self):
        """
        el metodo destructor simplemente destruye el objeto
        :return:
        """
        pass

    def suma(self, otherPoint):
        """
        Este metodo es una forma alterntiva de realizar la suma
        :param otherPoint: Objeto de la clase Punto
        :return: tupla con la suma de (x+x, y+y)
        """
        sumaX = self.x + otherPoint.x
        sumaY = self.y + otherPoint.y
        return  (sumaX, sumaY)

    def printPoint(self):
        """
        Este metodo imprime las coordenas x,y del objeto
        :return: None
        """
        print("(", self.__x, ",", self.__y, ")")
        print(" ")

    def calDist(self, other):
        """
        Este metodo se utiliza obtener la distancia entre dos puntos
        :param other: objeto de la clase Punto al que se medirá la distancia
        :return: distancia entre los puntos self y other
        """
        dist = (((other.__x - self.__x)**2) + ((other.__y - self.__y)**2))**(1/2)
        return dist

    #Declaracion Getters
    def getX(self):
        """
        Método para accesar al atributo __x
        :return: atributo __x
        """
        return self.__x

    def getY(self):
        """
        Método para acceder al atributo __y
        :return: atributo __y
        """
        return self.__y

    #Declarar Setters
    def setX(self, newX):
        """
        Método para cambiar el atributo __x
        :param newX: nuevo valor para el atributo
        :return: None
        """
        self.__x = newX

    def setY(self, newY):
        """
        Método para cambiar el atributo __y
        :param newY: nuevo valor para el atributo
        :return:
        """
        self.__y = newY

    #Sobrecarga de operadores
    def __add__(self, otroObjeto):
        sumaX = self.__x + otroObjeto.__x
        sumaY = self.__y + otroObjeto.__y
        return Punto(sumaX, sumaY)

    def __sub__(self, otroObjeto):
        restaX = self.__x - otroObjeto.__x
        restaY = self.__y - otroObjeto.__y
        return Punto(restaX, restaY)

    def __mul__(self, otroObjeto):
        mulX = self.__x * otroObjeto.__x
        mulY = self.__y * otroObjeto.__y
        return Punto(mulX, mulY)

    def __truediv__(self, otroObjeto):
        divX = self.__x / otroObjeto.__x
        divY = self.__y / otroObjeto.__y
        return Punto(divX, divY)
