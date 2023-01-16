# GENERADORES
'''
Es una especie de función que se utiliza para generar secuencias de valores. A diferencia de las listas y otros tipos de datos que almacenan todos los valores en la memoria, los generadores generan valores sobre la marcha, lo que los hace más eficientes en términos de uso de memoria.
'''
# lista = []
# def generar_impares(n):
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             lista.append(i)
#     return lista
# impares = generar_impares(10)
# print('impares: ', impares)

# def generar_impares(n):
#     for i in range(1, n+1):
#         if i % 2 != 0:
#             yield i
# impares = generar_impares(9)

# print(next(impares))
# print("varias lineas de codigo")
# print(next(impares))
# print("varias lineas de codigo")
# print(next(impares))

# def nombres(*name):
#     for x in name:
#         for z in x:
#             yield z
# res = nombres("Sofia", "Luis", "Dayana")
# print(next(res))
# print(next(res))
# print(next(res))

def nombres(*name):
    for x in name:
        yield from x #sirve para delegar la generacion valores de un generador a otro
res = nombres("Sofia", "Luis", "Dayana")
print(next(res))
print(next(res))
print(next(res))