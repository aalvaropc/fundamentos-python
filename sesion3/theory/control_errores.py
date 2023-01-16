
'''
ERRORES DE SINTAXIS
El código escrito no es una expresión valida en Python, muy facil de detectar
'''
# print("hola"

'''
ERROR DE TIEMPO DE EJECUCIÓN
El codigo es correcto pero en ocasiones al ejecutarse falla
'''
# lista = []
# print(lista[0])

# import random
# a = random.randint(0, 3)
# if a%2 == 0:
#     print("El numero es par")
# else:
#     print(1/0)

'''
ERROR SEMANTICO
Errores dificiles de detectar, ya que el codigo es correcto y se ejecuta sin problemas

Deseamos que una expresión sea True si un valor entero no está en el intervalo 0 <= valor <=3 
'''
# valor = 4
# resultado = valor < 0 and valor > 3  # La conectiva lógica correcta es or
# print(resultado)

#TIPOS DE EXCEPCIONES(BUILT-IN EXCEPTIONS)
'''
TypeError -> Cuando se aplica una operación o función a un dato del tipo inapropiado.
ZeroDivisionError -> Cuando se itenta dividir por cero.
OverflowError -> Cuando un cálculo excede el límite para un tipo de dato numérico.
IndexError -> Cuando se intenta acceder a una secuencia con un índice que no existe.
KeyError -> Cuando se intenta acceder a un diccionario con una clave que no existe.
FileNotFoundError -> Cuando se intenta acceder a un fichero que no existe en la ruta indicada.
ImportError -> Cuando falla la importación de un módulo.
'''


# ESTRUCTURA CONDICIONAL Try except
'''
try:
    #se prueba este codigo
    #linea1
    #linea2
    #linea3
    #excepcion
    #linea5
except TipoDeExcepcion:
    #se ejecuta este codigo si ocurre un error
else:
    #se ejecuta si el bloque try se ejecuta sin errores
finally:
    #se ejecuta siempre
'''


# PRUEBA Y EXCEPCION DE LOS BLOQUES
# try:
#     numero = int(input("Ingrese un numero entero: "))
# except :
#     print("Algo salio mal", ValueError)


# try:
#     result = 1/0
#     print("El resultado es:",result)
#     x = y + 1
#     print("La variable x es:",x)
# except ZeroDivisionError:
#     print("No es posible dividir por cero.")
# except NameError:
#     print("La variable y no ha sido definida.")
# else:
#     print("El bloque try se ha ejecutado sin errores.")
# finally:
#     print("Este bloque se ejecutará siempre.")



# RAISE -> Se utiliza para generar una excepción manualmente
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("No se puede dividir por cero")
    return a / b
print(divide(2, 0))