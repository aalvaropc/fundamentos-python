# Clases
class Persona:
    nombre = "Valeria" #atributo
    edad = 21

persona1 = Persona()
print(persona1.nombre)
print(persona1.edad)

persona2 = Persona()
persona2.nombre = "Lucia"
persona2.edad = 20
print(persona2.nombre)
print(persona2.edad)

##########################

#Metodo
class Operacion:
    def suma(self):
        self.n1 = 20
        self.n2 = 10
op = Operacion()
op.suma()
print(op.n1 + op.n2)

##########################

# Constructor
class Operacion:
    def __init__(self, n1, n2):
        self.suma = n1 + n2
        self.resta = n1 - n2

op = Operacion(12, 23)
print(op.resta)

class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

persona1 = Persona("Luis", 12)
print(persona1.edad)
print(persona1.nombre)