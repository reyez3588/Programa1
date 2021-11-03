"""
Excepciones II
"""
"""
try:
    intentar realizar esto
except "X":
    Realizar algo si encuentra el error "X"
else:
    esta sección de código se corre cuando no se encuentra ningún error
    
"""


try:
    opcion = int(input("Ingrese un numero: \n 1 para error de memoria \n 2 para error de nombre \n"))
    if opcion == 1:
        raise StopAsyncIteration
    if opcion == 2:
        raise NotImplementedError
except (MemoryError, ValueError, StopAsyncIteration):
    print("Usted eligió el error de memoria o ingresó una letra")
except NotImplementedError:
    print("Usted eligió el error de nombre")
else:
    print("El número que usted eligió no es el adecuado")

print("El flujo del programa ha llegado a este punto")