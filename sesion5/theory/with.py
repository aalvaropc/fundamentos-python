# Uso de "with", se encarga automáticamente de cerrar el archivo al finalizar el bloque de código

# Lectura de un archivo
with open("texto.txt", "r") as archivo:
    texto = archivo.read()
    print(texto)

# Escritura de un archivo
with open("texto.txt", "w") as archivo:
    archivo.write("Hola mundo!")

# Añadir contenido a un archivo
with open("texto.txt", "a") as archivo:
    archivo.write("\nAñadiendo más contenido al archivo.")

# Leer y escribir un archivo al mismo tiempo
with open("texto.txt", "r+") as archivo:
    texto = archivo.readlines()
    texto[1] = "He modificado la linea 2\n" #cambiara la linea 2 del archivo de texto
    archivo.seek(0)
    archivo.writelines(texto)