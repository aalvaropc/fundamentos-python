# Funciones

# Funciones sin argumentos
def saludo():
    print("Hola")
# saludo() # invocar la funcion


# Valor que devuelve la funcion
# salida = saludo()
# print(salida) #None, denota falta de valor

# Return
def saludo2():
    return "Hola"

resultado = saludo2()
# print(f"{resultado=}")

# Argumentos opcionales y requeridos
# Algunas funciones integradas en python requieren argumentos, mientras otras hacen que los argumentos sean opcionales

# any() -> Toma un objeto iterable y devuelve True si algun elemento del objeto iterable es True, de lo contrario False

mi_list = [0, False, [], None, 1]
value = any(mi_list)
print(f"{value=}")

# str() -> convierte un objeto a cadena, argumento opcional
# str()

# Uso de argumentos de funcion en Python
# Exigencia de un argumento

def es_mayor_de_edad(edad):
    return edad >= 18


def saludar(edad, nombre = "Alvaro", clima = "frío"):
    return f"Hola mi nombre es {nombre} y tengo {edad}, y mi clima es {clima}"

resultado = saludar(nombre = "Juan", edad = 22)
print(f"{resultado=}")


# Funciones como argumentos
def redondear():
    return 12.83843
valor = round(redondear(), 2)
print(f"{valor=}")


# Argumentos de variables
# permiten pasar cualquier cantidad de argumentos
def promedio_edades(*args): # *args -> indica que es una tupla, es una convencion "args"
    return sum(args)/len(args)
resultado = promedio_edades(12, 13, 14, 15, 16)
print(f"{resultado=}")

# Argumentos de palabra clave variable
def notas_alumnos(**kw): # **kwargs -> indica que es un diccionario, es una convencion "kwargs"
    for alumno, nota in kw.items():
        print(f"{alumno} tiene una nota de {nota}")
    return kw
n_a = notas_alumnos(alumno1 = 12, alumno2 = 13, alumno3 = 14, alumno4 = 15)
print(n_a)



