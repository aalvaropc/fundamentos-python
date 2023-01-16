# FUNCIONES LAMBDA
'''
La palabra clave lambda crea una función en línea que contiene una sola expresión. El valor de esta expresión es lo que devuelve la función cuando se invoca
'''

# SIN ARGUMENTOS
def saludo():
    return "Hola"

print(saludo())

saludar = lambda:"Hola"
print(saludar())

# CON ARGUMENTOS
mensaje = "     Hola     "
cambio = lambda x: x.upper().strip()
print(cambio(mensaje))

alumnos = {"Juan":12, "Ana":19, "Maria":16}
mostrar_alumnos = lambda kw: [f"El alumno {k} tiene {v}\n" for k,v in kw.items()]
print("".join(mostrar_alumnos(alumnos)))

#NOTA -> PEP-8 no recomienda asignar lambdas a las variables 


def f(x): return 2 ** x

f = lambda x : x ** 2

