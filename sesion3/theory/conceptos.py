# FUNCIONES PURAS
def suma(num1, num2):
    return num1 + num2

# print(suma(2, 5))
# print(suma(2, 5))
# print(suma(2, 5))
# print(suma(2, 5))

total = 0
def suma2(num1, num2):
    global total
    
    total += num1 + num2

    return total
# print(suma2(2, 5))
# print(suma2(2, 5))
# print(suma2(2, 5))
# print(suma2(2, 5))
# print(suma2(2, 5))


# COMPOSICIÓN DE FUNCIONES
def cuadrado(numero):
    return numero**2

def suma_cuadrados(num1, num2):
    return cuadrado(num1) + cuadrado(num2)

def cuadrado_antecesor_sucesor(num):
    return suma_cuadrados(num-1, num+1)

# print(cuadrado_antecesor_sucesor(3))

# FUNCIONES RECURSIVAS
def triplicar_lista(lista):
    if(len(lista) == 1):
        return [lista[0] * 3]
    else:
        return [lista[0]*3] + triplicar_lista(lista[1:])
mi_lista = [2, 5, 3, 7]
print(triplicar_lista(mi_lista))


# FUNCIONES DE ALTO ORDEN

def accion(n):
    return n  * 3

def mapear_lista(lista, accion):
    if(len(lista) == 1):
        return [accion(lista[0])]
    else:
        return [accion(lista[0])] + mapear_lista(lista[1:], accion)
mi_lista = [2, 5, 3, 7]
print(mapear_lista(mi_lista, accion))
