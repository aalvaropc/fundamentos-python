# Es una técnica para asignar los elementos de una secuencia (como una lista o tupla) a variables individuales

marcas = ['Chevrolet', 'Honda', 'Kia', 'Toyota']

marca1, marca2, marca3, marca4 = marcas
print(marca1, marca2, marca3, marca4)

# PROBLEMAS AL DESEMPAQUETAR
# Muchos valores para desempaquetar
# marca1, marca2, marca3 = marcas
# print(marca1, marca2, marca3)

# No hay suficientes valores para desempaquetar
# marca1, marca2, marca3, marca4, marca5 = marcas
# print(marca1, marca2, marca3, marca4, marca5)



# Operadores de desempaquetado

# Caso: Obtener el ultimo y primer elemento de una lista sin usar indices
first, *_, last = [23, 12, 54, 76, 83, 30]
print(first, last, _)

# Descomprimir todos los valores en una sola variable
*cadena, = 'Python'
print('cadena: ', cadena)

# Para secuencia de números, empaquetado de números
*numbers, = range(7)
print('numbers: ', numbers)

# Desempaquetar diccionarios
my_dict = {'one': 1, 'two':2, 'three': 3, 'four': 4, 'five':5}
val1, *_, val2 = my_dict #LLaves
print('val1, val2: ', val1, val2)

val1, *_, val2 = my_dict.values() #LLaves
print('val1, val2: ', val1, val2)

val1, *_, val2 = my_dict.items() #Key-value
print('val1, val2: ', val1, val2)


