#FUNCIONES DE ORDEN SUPERIOR
'''
Son aquellas que aceptan otras funciones como argumentos o devuelven funciones como resultado
Permiten una mayor flexibilidad en el diseño de código y una mejor reutilización de código
'''
def operar(x, funcion):
    return funcion(x)

def sqrt(y):
    return y**0.5

def cuadrado(z):
    return z**2

resultado = operar(4, sqrt)
print(resultado)


#MAP
'''
map(funcion, iterable)
Aplica una función dada a cada elemento de un iterable (por ejemplo, una lista) y devuelve un iterador con los resultados
'''
numbers = [1,2,3,4,5]
cubo = list(map(lambda x: x**3, numbers))
print(cubo)

list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = [7, 8, 9]
resultado = map(lambda x, y, z: x + y + z, list1, list2, list3)
print(list(resultado))

#FILTER
'''
filter(function, iterable)
Filtra los elementos de un iterable según una función dada y devuelve un iterador con los elementos que cumplen la condición.
'''
numeros = [23, 43, 13, 76, 89, 56, 34, 7, 92]
pares = list(filter(lambda x: x % 2 == 0, numeros))
print(pares)

frutas = ["manzana", "pera", "sandia", "naranja", "melon", "uva"]
empieza_m = list(filter(lambda x: x[0] == "m", frutas))
print(empieza_m)

#REDUCE
'''
reduce(function, iterable)
Aplica una función dada de forma acumulativa a los elementos de un iterable y devuelve un único resultado. Este funcion esta en el modulo functools.
'''

#NOTA: Es necesario importarla, ya que no viene integrada
from functools import reduce

numeros2 = [1,2,3,4,5,6,7,8,9,10]
#[3,3,4,5,6,7,8,9,10]
#[6,4,5,6,7,8,9,10]
suma_acumulada = reduce(lambda x, y: x + y, numeros2)
print(suma_acumulada)


numero = 3
factorial = reduce(lambda x, y: x * y, range(1, numero + 1))
print('factorial: ', factorial)
