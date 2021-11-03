
"""CONSTRUCTORES Y DESTRUCTORES
Crear una clase basada en CNCs"""

class CNC:
    #MÉTODO CONSTRUCTOR
    def __init__(self, numEjes, dimensiones, costo, cantHerramientas, tipoControlador):
        self.numEjes = numEjes
        self.dimensiones = dimensiones
        self.costo = costo
        self.cantHerramientas = cantHerramientas
        self.tipoControlador = tipoControlador
        print("Has creado un objeto de la clase CNC, con : ", self.numEjes, "ejes")

    def __carear(self):
        print("Estoy careando")
        return

    """
    def desbastar(self):
        print("Estoy desabastando")
        return
    """

    def desbastar(self, nPiezas = None):
        if nPiezas == None:
            print("No hay pieza a desbastar")
        else:
            print("Estoy desabastando", nPiezas, "piezas")
        return

    def moletear(self):
        print("Estoy moleteando")
        return

    #Método DESTRUCTOR
    def __del__(self):
        print("Has destruido el objeto")
        return


"""ACA INICIA EL PROGRAMA PRINCIPAL"""
torno = CNC(4, "200x200", 3000000, 15, "FANUC")
torno._CNC__carear()
torno.desbastar()
torno.desbastar(25)

#torno.carear()
#centroMaquinado = CNC(6, "300x500", 7000000, 20, "FANUC")
#centroMaquinado.desbastar()




