"""
Excepciones
"""


def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def mult(num1, num2):
    return num1 * num2

def div(num1, num2):
    try:
        return num1 / num2
    except ZeroDivisionError:
        print("La división por cero no es posible...")

while True:
    numero1 = input("Ingrese el primer número: ")
    numero2 = input("Ingrese el segundo número: ")

    try:
        numero1 = float(numero1)
        numero2 = float(numero2)
        break
    except ValueError:
        print("Por favor ingrese solo números")

result = mult(numero1, numero2)
print(result)

print("El programa ha llegado a este punto")

