# METODOS ESPECIALES O DUNDER METHODS
# se utilizan para definir comportamientos específicos para una clase

# __str__,  define la representación en cadena de un objeto de una clase
class Coche:
    def __init__(self, marca, color, velocidad):
        self.marca = marca
        self.color = color
        self.velocidad = velocidad

    def avanzar(self):
        return f"EL auto avanzo {self.velocidad}m"
    
    def __str__(self):
        return f"Es un auto marca {self.marca} y es color {self.color}"        

coche1 = Coche("Toyota", "Azul", 50)
print(coche1.marca)
print(coche1.color)

print(coche1.avanzar())

coche2 = Coche("Honda", "Negro", 60)
print(coche2.marca)
print(coche2.color)

print(coche2.avanzar())

print(coche1)
print(coche2)

# __adD__, es llamado cuando se intenta sumar dos instancias de una clase usando el operador +
class Numero:
    def __init__(self, valor):
        self.valor = valor
    def __add__(self, otro):
        return Numero(self.valor + otro.valor)

n1 = Numero(5)
n2 = Numero(10)
n3 = n1 + n2
print(n3.valor)

# __len__, es llamado cuando se intenta obtener el tamaño de una instancia de una clase usando la función len()
class Lista:
    def __init__(self, elementos):
        self.elementos = elementos
    def __len__(self):
        return len(self.elementos)

mi_lista = Lista([1,2,3,4])
print(len(mi_lista)) # imprime 4

# __getitem__, es llamado cuando se intenta acceder a un elemento de una instancia de una clase usando corchetes
class Frase:
    def __init__(self, texto):
        self.texto = texto
    def __getitem__(self, index):
        return self.texto[index]

f = Frase("Hola mundo")
print(f[4]) # imprime "o"

# __call__, es llamado cuando se intenta llamar a una instancia de una clase como si fuera una función
class Sumador:
    def __init__(self, valor):
        self.valor = valor
    def __call__(self, otro_valor):
        return self.valor + otro_valor

s = Sumador(5)
print(s(10)) # imprime 15

# __del__, es llamado cuando se elimina una instancia de una clase
class Archivo:
    def __init__(self, nombre):
        self.nombre = nombre
    def __del__(self):
        import os
        os.remove(self.nombre)

a = Archivo("temp.txt")
del a # elimina el archivo "temp.txt"