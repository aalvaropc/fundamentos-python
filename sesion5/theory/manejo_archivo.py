# from io import *
from os import path


def escribir_archivo():
    archivo = open('Texto.txt', 'w') #Modo escritura
    archivo.write("Este es un mensaje2")
    archivo.close()


def leer_archivo():
    # archivo = open("Texto.txt", "r") #Modo lectura
    # print(archivo.read())
    # archivo.close()

    
    # try:
    #     archivo = open("Texto.txt", "r") #Modo lectura
    #     print(archivo.read())
    #     archivo.close()
    # except FileNotFoundError as e:
    #     print(e)
    

    #Otra forma
    # if path.isfile("Texto.txt"):
    #     archivo = open("Texto.txt", "r") #Modo lectura
    #     print(archivo.read())
    #     archivo.close()
    # else:
    #     print("No existe el archivo")


    #Metodo readlines
    if path.isfile("Texto.txt"):
        archivo = open("Texto.txt", "r") #Modo lectura
        contenido = archivo.readlines()
        print(contenido)
        archivo.close()
    else:
        print("No existe el archivo")
# leer_archivo()
def agregar_datos(): #esto no borrara el contenido como el flujo de escribir
    if path.isfile("Texto.txt"):
        archivo = open("Texto.txt", "a") #Modo actualizar
        archivo.write("\nHola este es un mensaje agregado")
        archivo.close()
    else:
        print("No existe el archivo")
# agregar_datos()

def modificar_datos():
    if path.isfile("Texto.txt"):
        archivo = open("Texto.txt", "r+") #Modo lectura y escritura
        texto = archivo.readlines()
        print(texto) #para verificar que tiene el archivo de texto
        texto[1] = "He modificado la linea 2\n" #esto cambiara la linea 2 del archivo de texto
        print(texto)
        archivo.seek(0)#para reescribir todo elarchivo de texto usamos en puntero con el metodo seek 
        archivo.writelines(texto)
        archivo.close()
        print(texto)
    else:
        print("No existe el archivo")


def eliminar_datos():
    archivo = open("Texto.txt", "w")
    archivo.close()
eliminar_datos()
