"""
Es la capacidad de un objeto de tomar varias formas. Esto se logra mediante la sobrecarga de operadores y la sobreescritura de métodos.
"""
class Persona(object):
    def __init__(self, nombre):
        self.nombre = nombre
    
    def moverse(self):
        print("Caminando...")

class Nadador(Persona):
    def moverse(self):
        print("Nadando..")
class Ciclista(Persona):
    def moverse(self):
        print("Pedaleando..")

persona = Persona("Andres")
persona.moverse()

nadador = Nadador("Luis")
nadador.moverse()

ciclista = Ciclista("Luciana")
ciclista.moverse()