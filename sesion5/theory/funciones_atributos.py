# getattr, Obtiene el valor de un atributo de manera directa
class Animal:
    def __init__(self, nombre, peso, color):
        self.nombre = nombre
        self.peso = peso
        self.color = color
cat = Animal("gato", 1.4, "Blanco")
# print(cat.nombre)
# print(getattr(cat, "peso"))

# hasattr, determina si un objeto tiene un artibuto especifico
class Laptop:
    def __init__(self, marca, modelo, bateriaPrincipal):
        self.marca = marca
        self.modelo = modelo
        self.bateriaPrincipal = bateriaPrincipal
miLaptop = Laptop("HP", "2019", 1500)
# print("La latop tiene bateria secundaria?", "Si" if hasattr(miLaptop, "bateriaSecundaria") else "No")

# setattr, establece el valor de un atributo existente y puede crear el valor de un atributo no existente
# atributo existente
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Auto("Toyota", "Yaris")
setattr(mi_auto, "marca", "Honda")
# print(mi_auto.marca)

# Crear y establecer el valor de un atributo no existente
class Auto:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Auto("Toyota", "Yaris")
setattr(mi_auto, "color", "Azul")
# print(mi_auto.color)


# delattr, eliminar atributos

# Eliminar un atributo existente
class Auto2:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Auto2("Toyota", "Yaris")
delattr(mi_auto, "marca")
try:
    print(mi_auto.marca)
except AttributeError as e:
    print("El atributo no existe")

# Eliminar un atributo no existente
class Auto3:
    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo

mi_auto = Auto3("Toyota", "Yaris")

try:
    delattr(mi_auto, "color")
except AttributeError as e:
    print("El atributo color no existe")


# Casos
# Atributo para un solo metodo
class Animal2:
    def __init__(self, nombre, peso, color):
        self.nombre = nombre
        self.peso = peso
        self.color = color
    def descripcion(self):
        return f"El animal se llama {self.nombre}"
    
    def sonido(self, sonido):
        return f"El {self.nombre} dice {sonido}"
gato = Animal2("gato", 2, "negro")
print(gato.descripcion())
print(gato.sonido("Miau"))
