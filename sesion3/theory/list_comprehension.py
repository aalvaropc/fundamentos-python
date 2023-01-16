# LIST COMPREHENSION
'''
Las listas de comprensión en Python son construcciones sintácticas concisas. Se pueden utilizar para generar listas a partir de otras listas aplicando funciones a cada elemento de la lista.

[ <expresion> for <elemento> in <iterable> ]
[ <expresion> for <elemento> in <iterable> if <condicion>]
''' 

cuadrados = [x**2 for x in range(1, 11)]
print('cuadrados: ', cuadrados)


mensaje = [y.lower() for y in "BUENAS TARDES"]
print('mensaje: ', mensaje)


pares = [x for x in range(1, 21) if x%2 == 0]
print('pares: ', pares)


matriz = [[i*j for i in range(1, 4)] for j in range(1, 4)]
print(matriz)

# {clave: valor for x in iterable}
personas = [("Juan", 25), ("Ana", 22), ("Maria", 30)]
edad_por_nombre = {nombre: edad for nombre, edad in personas}
print(edad_por_nombre)