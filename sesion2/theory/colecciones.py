#COLECCIONES

#1.listas

#Crear lista vacia
lista_Vacia = []
lista_Vacia2 = list()

#Crear una lista con elementos
mi_lista = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
mi_lista2 = ["Hola", "Mundo", 1, .3, True]
mi_lista3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(mi_lista, mi_lista2, mi_lista3)
# print(type(mi_lista))

#Acceder a un elemento de una lista
primer_elemento = mi_lista[0]
segundo_elemento = mi_lista2[1]
elemento = mi_lista[-4]
# print(elemento)

#Modificar elementos de una lista
mi_lista[0] = 200
# print(mi_lista)

#SLICING
# lista[start:stop:step]
elements1 = mi_lista[2:5]
elements2 = mi_lista[:3]
elements3 = mi_lista[5:]
elements4 = mi_lista[-5:-2]
elements5 = mi_lista[2:8:2]
elements6 = mi_lista[::3]
elements7 = mi_lista[::-1]
# print(elements1)

#metodos para listas
listap = []

#append() -> añade un elemento al final de una lista
listap.append("Hola")
# print(listap)

#extend() -> añade varios elementos al final de una lista
listap.extend([1, 2, 3, 4, 5])
# print(listap)

#insert() -> inserta un elemento en una posición dada
listap.insert(1, "Mundo")
# print(listap)

#remove() -> elimina el primer elemento coincidente de la lista
listap.remove("Hola") #Devuelve un error si no se encuentra el elemento
# print(listap)

#pop() -> Elimina el elemento segun su posición y lo devuelve. Si no se especifica un índice, se elimina el último elemento.
val = listap.pop(3)
# print(listap)
# print(f"{val=}")

#index() -> devuelve el índice del elemento especificado en la lista
indice = listap.index("Mundo")
# print(f"{indice=}")

#count() -> devuelve el número de veces que aparece un elemento en la lista
listap.extend([2, 2, 4, 4, 4, 4, 5, 6, 7])
cantidad_4 = listap.count(4)
# print(f"{cantidad_4=}")

#reverse() -> invierte la lista
listap.reverse()
# print(listap)

#sort() -> ordena los elementos de una lista en orden ascendente o descendente.
numbers = [12, 23, 1, 4, 67, 123, 45, 897, 45]
numbers.sort()
# print(numbers) #Ascendente
numbers.sort(reverse=True)
# print(numbers) #Descendente

#Eliminar con del un elemento de una lista
del numbers[0]
# print(numbers)

#del tambien sirve para eliminar variables y es una instruccion
del numbers[3:5]
# print(numbers)

#clear() -> elimina todos los elementos de una lista
listap.clear()
# print(listap)


#TUPLAS
mi_tupla = (2, 34, 12, 2, 87, 27, 56, 2)

# crear una tupla vacia
tupla_vacia = ()
tupla_vacia2 = tuple()

#acceder a un elemento de una tupla
element = mi_tupla[0]
# print(element)

#no se puede modificar un elemento de una tupla
# mi_tupla[0] = 23 #Devolvera un error

#count() -> Devuelve el número de veces que aparece un elemento en la lista
cant_2 = mi_tupla.count(2)
# print(f"{cant_2=}")

#index(x) -> Devuelve el índice del primer elemento de la tupla cuyo valor sea x.
indice_2 = mi_tupla.index(2)
# print(f"{indice_2=}")

indice_2x = mi_tupla.index(2, 1, 4)
# print(f"{indice_2x=}")


#DICCIONARIOS
#diccionario vacio
diccionariox = {}
# print(type(diccionariox))


diccionario = {'nombre': 'Juan', 'edad': 30, 'ciudad': 'Madrid'}

#Acceder a los elementos de un diccionario
nombre = diccionario['nombre']
# print(nombre)

#Modificar los elementos de un diccionario
diccionario['edad'] = 18
# print(diccionario['edad'])

#Obtener las llaves
llaves = list(diccionario.keys())
# print(llaves)

#Obtener los valores
valores = list(diccionario.values())
# print(valores)

#Buscando llave inexistente
# estado = diccionario['estado']

#Evitar la excepción KeyError
estado = diccionario.get('estado')
# print(f"{estado=}")

#Agregar clave y valor
# print(diccionario)
diccionario["pais"] = "España"
# print(diccionario)

#Establecer una clave y valor por defecto
cellphone = diccionario.setdefault("cellphone", "Movistar")
# print(diccionario)
# print(f"{cellphone=}")

#Copiar un diccionario
diccionario_copia = diccionario.copy()
# print(diccionario_copia)

#Crear un nuevo diccionario desde las claves de una secuencia
alumnos = ['Juan', 'Juana', 'Luis', 'Luisa', 'Fabian', 'Fabiana']

prom_alumnos = dict.fromkeys(alumnos) #Trae por defecto None
# print(prom_alumnos)

prom_alumnos = dict.fromkeys(alumnos, 0)
# print(prom_alumnos)

#Concatener diccionarios
diccionario1 = {'Iphone 12': 1800 , 'Samsung Galaxy S10': 2000}
diccionario2 = {'Xiaomi Redmi 9': 1000 , 'Moto g 8': 1500}
diccionario1.update(diccionario2)
# print(diccionario1)


#Eliminar con llave de un diccionario con del
del diccionario1['Iphone 12']
# print(diccionario1)

#Sets

#Crear un set vacio
mi_set1 = set()

mi_set2 = {0, 2, 3, 4, 4, 5, 5, 5, 7, 8, 8, 1, 1, 3}
# print('mi_set2: ', mi_set2)


lucia = {'l', 'u', 'c', 'i', 'a'}
# print('lucia: ', lucia)

#El set no ordena cadenas pero si numeros, pero esto no significa que esten ordenados realmente ya que esto solo pasa al momento de imprimirse

mi_set3 = {0, 1, 2, 3}

#Añadir un elemento a un conjunto
mi_set3.add(4)
# print('mi_set3: ', mi_set3)

#Añadir varios elementos a un conjunto
mi_set3.update([9, 10, 122])
# print('mi_set3: ', mi_set3)

#Remover un elemento de un conjunto
mi_set3.remove(4)
# print('mi_set3: ', mi_set3)

# Remover un elemento de un conjunto controlando la excepcion KeyError
mi_set3.discard(9999)
# print('mi_set3: ', mi_set3)

#OPERACIONES CON CONJUNTOS
conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {4, 5, 6, 7, 8}

# Unión de conjuntos con la operación '|'
union = conjunto_a | conjunto_b
# print(union)  # Imprime {1, 2, 3, 4, 5, 6, 7, 8}

# Unión de conjuntos con el método 'union()'
union = conjunto_a.union(conjunto_b)
# print(union)  # Imprime {1, 2, 3, 4, 5, 6, 7, 8}

# Intersección de conjuntos con la operación '&'
interseccion = conjunto_a & conjunto_b
# print(interseccion)  # Imprime {4, 5}

# Intersección de conjuntos con el método 'intersection()'
interseccion = conjunto_a.intersection(conjunto_b)
# print(interseccion)  # Imprime {4, 5}

# Diferencia de conjuntos con la operación '-'
diferencia = conjunto_a - conjunto_b
# print(diferencia)  # Imprime {1, 2, 3}

# Diferencia de conjuntos con el método 'difference()'
diferencia = conjunto_a.difference(conjunto_b)
# print(diferencia)  # Imprime {1, 2, 3}

# Frozenset
# Son utiles cuando necesitamos un conjunto de elementos que no va a cambiar durante la ejecución del programa

# Crear un frozenset
frozen_conjunto = frozenset({1, 2, 3, 4, 4, 5})
# print('frozen_conjunto: ', frozen_conjunto)


# Alunas built-in functions que se pueden utilizar con colecciones

# 1. len(coleccion)
lista = [1, 2, 3, 4, 5]
tupla = (1, 2, 3, 4, 5)
conjunto = {1, 2, 3, 4, 5}
diccionario = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

# Longitud de una lista
longitud_lista = len(lista)
# print('longitud_lista: ', longitud_lista) # Imprime 5

# Longitud de una tupla
longitud_tupla = len(tupla)
# print('longitud_tupla: ', longitud_tupla) # Imprime 5

# Longitud de un conjunto
longitud_conjunto = len(conjunto)
# print('longitud_conjunto: ', longitud_conjunto) # Imprime 5

# Longitud de un diccionario
longitud_diccionario = len(diccionario)
# print('longitud_diccionario: ', longitud_diccionario) # Imprime 5

# 2. max(coleccion)

# Elemento máximo de una lista
maximo_lista = max(lista)
# print('maximo_lista: ', maximo_lista) # Imprime 5

# Elemento máximo de una tupla
maximo_tupla = max(tupla)
# print('maximo_tupla: ', maximo_tupla) # Imprime 5

# Elemento máximo de un conjunto
maximo_conjunto = max(conjunto)
# print('maximo_conjunto: ', maximo_conjunto) # Imprime 5

# Elemento máximo de un diccionario
maximo_diccionario = max(diccionario)
# print('maximo_diccionario: ', maximo_diccionario) # Imprime 'e'

# 3. min(coleccion)

# Elemento mínimo de una lista
minimo_lista = min(lista)
# print('minimo_lista: ', minimo_lista) # Imprime 1

# Elemento mínimo de una tupla
minimo_tupla = min(tupla)
# print('minimo_tupla: ', minimo_tupla) # Imprime 1

# Elemento mínimo de un conjunto
minimo_conjunto = min(conjunto)
# print('minimo_conjunto: ', minimo_conjunto) # Imprime 1

# Elemento mínimo de un diccionario
minimo_diccionario = min(diccionario)
# print('minimo_diccionario: ', minimo_diccionario) # Imprime 1

# 4. sum(coleccion)

# Suma de los elementos de una lista
suma_lista = sum(lista)
# print('suma_lista: ', suma_lista) # Imprime 15

# Suma de los elementos de una tupla
suma_tupla = sum(tupla)
# print('suma_tupla: ', suma_tupla) # Imprime 15

# Suma de los elementos de un conjunto
suma_conjunto = sum(conjunto)
# print('suma_conjunto: ', suma_conjunto) # Imprime 15

# Suma de los elementos de un diccionario
suma_diccionario = sum(diccionario.values())
# print('suma_diccionario: ', suma_diccionario) # Imprime 15

# 5. sorted(coleccion)
lista2 = [5, 3, 1, 4, 2]
# Ordenar los elementos de una lista

lista_ordenada = sorted(lista2)
# print('lista_ordenada: ', lista_ordenada) # Imprime [1, 2, 3, 4, 5]

# Ordenar los elementos de una lista en orden inverso
lista_ordenada = sorted(lista2, reverse=True)
# print('lista_ordenada: ', lista_ordenada) # Imprime [5, 4, 3, 2, 1]

# 6. zip()

# Combinar elementos de dos listas
lista_a = [1, 2, 3, 4]
lista_b = ['a', 'b', 'c', 'd']
parejas_lista = list(zip(lista_a, lista_b))
# print('parejas_lista: ', parejas_lista) # Imprime [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]

# Combinar elementos de dos tuplas
tupla_a = (1, 2, 3, 4)
tupla_b = ('a', 'b', 'c', 'd')
parejas_tupla = tuple(zip(tupla_a, tupla_b))
# print('parejas_tupla: ', parejas_tupla) # Imprime ((1, 'a'), (2, 'b'), (3, 'c'), (4, 'd'))

# Combinar elementos de dos conjuntos
conjunto_a = {1, 2, 3, 4}
conjunto_b = {'a', 'b', 'c', 'd'}
parejas_conjunto = set(zip(conjunto_a, conjunto_b))
# print('parejas_conjunto: ', parejas_conjunto) # Imprime {(4, 'b'), (2, 'c'), (1, 'a'), (3, 'd')}

alumnos = ['Sofia', 'Carlos', 'Luciana', 'Francisco']
notas = [13, 12, 15, 14]
relacion = list(zip(alumnos, notas))
# print('relacion: ', relacion)

#range() -> genera una secuencia de números enteros en un intervalo determinado

numbers1_10 = list(range(1, 20, 2))
# print('numbers1_10: ', numbers1_10)

