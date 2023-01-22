#Como ver los modulos integrados
print(help("modules"))

import math
from math import isqrt
print(help(math))
print(pow(2, 3)) # potencia
print(isqrt(64)) #raiz cuadrada

import os
import sys


#Obtener la ruta del directorio actual
direccion_actual = os.getcwd()
# print('direccion_actual: ', direccion_actual)

# Crear directorios
# os.mkdir("Nueva carpeta")

# Eliminar un directorio
# os.rmdir("Nueva carpeta")

# Eliminar archivos
# os.remove("mi_block.txt")

# Cambiar el nombre de un arhivo
# os.rename("implementacion.py", "implement.py")

# Listar archivos del directorio actual
# print(os.listdir())

# SYS

# Obtener la version de python
# print(sys.version)

# Obntener el nombre del sistema operativo
# print(sys.platform)

# Acceder al path del directorio actual
# print(sys.path)



from datetime import *

# Obtener la fecha actual
# print(datetime.now())

# Crear fechas
cumple = datetime(2023, 7, 12)
# print(cumple)

# Obtener partes de una fecha
fecha_actual = datetime.now()
# print(fecha_actual.year)    # Output: 2020
# print(fecha_actual.month)   # Output: 9
# print(fecha_actual.day)     # Output: 17
# print(fecha_actual.hour)    # Output: 11
# print(fecha_actual.minute)  # Output: 14
# print(fecha_actual.second)  # Output: 48

# Formatear una fecha a cadena
fecha_formateada = fecha_actual.strftime('%d/%m/%Y %H:%M:%S')
# print(fecha_formateada)

# Random
import random

# Generar un numero aleatorio del 1 al 100
numero_ale = random.randint(1, 3)
print(numero_ale)

# Seleccionar un elemento aleatorio de una lista
nombres = ["Juan", "Juana", "Luis", "Luisa"]
ganador = random.choice(nombres)
print(ganador)

# Barajar los elementos de una lista
numeros = [2, 34, 12, 76, 345, 23, 98, 46, 97, 15]
random.shuffle(numeros)
print(numeros)


import time

# Crear un delay
# print("Espera ..")
# time.sleep(10)
# print("Termino")

# print("Empezo la cuenta")
# for i in range(1, 11):
#     print(f"{i}%")
#     time.sleep(1)
# print("Termino la cuenta")

for i in range(1,21):
    sys.stdout.write(f"\r{i}%")
    time.sleep(0.5)
    sys.stdout.flush()
