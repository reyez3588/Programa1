

#print("hola Meca")

class Usuarios:
    def __init__(self, nid, alias, nombre, apellidos, password):
        self.nid = nid
        self.alias = alias
        self.nombre = nombre
        self.apellidos = apellidos
        self.__password = password

    def muestra_datos(self):
        print("El nombre y los apellidos del usuario son: ", self.nombre, self.apellidos)
        print("El ID es: ", self.nid)
        print("El alias del usuario es: ", self.alias)

    #Getters
    def get_password(self):
        return self.__password
    #Setters


class Cuenta:
    def __init__(self, propietario, saldo, moneda):
        self.__propietario = propietario
        self.__saldo = saldo
        self.__moneda = moneda


user1 = Usuarios(4, "Reyez", "Jesus", "Reyes Gomez", "351988")
user1.muestra_datos()
print(user1.get_password())

cuenta1 = Cuenta("Jesus", 1150, "pejeCoins")