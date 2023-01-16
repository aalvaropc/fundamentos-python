# SCOPE DE UNA VARIABLE
# LEGB = LOCAL -> ENCLOSED -> GLOBAL -> BUILT-IN

# CASO1
# nombre = "Juan"
# def mi_nombre():
#     nombre = "Juana"
#     print(f"Mi nombre detro de la función, {nombre}")

# mi_nombre()

# print(f"Mi nombre fuera de la función, {nombre}")

# CASO2
# def func1():
#     x = 1
#     print(x)

# func1()

# def func2():
#     x = 2
#     print(x)
# func2()

# func1()

# FUNCIONES ANIDADAS
# def func1():
    
#     def func2():
#         x = 1
#     func2()

# func1()

# GLOBAL
nombre = "Juan"
def mi_nombre():
    global nombre
    nombre = "Juana"
    print(f"Mi nombre detro de la función, {nombre}")

mi_nombre()

print(f"Mi nombre en el area local es, {nombre}")

# BUILT-IN
from math import pi
def print_pi():
    print(pi)
print_pi()

pi = 12
print(pi)
