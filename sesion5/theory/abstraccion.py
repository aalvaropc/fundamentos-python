"""
Es la capacidad de enfocarse en los aspectos esenciales de un objeto, ignorando los detalles irrelevantes
"""
# Ejemplo 1
class Vehiculo: #Es una abstracción de los diferentes tipos de vehículos que pueden avanzar
    def avanzar(self):
        pass

class Coche(Vehiculo):
    def avanzar(self):
        print("El coche ha avanzado.")

class Moto(Vehiculo):
    def avanzar(self):
        print("La moto ha avanzado.")

coche = Coche()
coche.avanzar()

moto = Moto()
moto.avanzar()

# Ejemplo 2
class Figura:
    def area(self):
        pass

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado**2

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return 3.14 * (self.radio**2)

cuadrado = Cuadrado(5)
print(cuadrado.area())

circulo = Circulo(3)
print(circulo.area())