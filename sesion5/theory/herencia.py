#Herencia basico
class Animal:
    def __init__(self, nombre, peso):
        self.nombre = nombre
        self.peso = peso
    
    def descripcion(self):
        return f"El {self.nombre} es un animal que pesa {self.peso}Kg"
class Aguila(Animal):
    def volar(self, altura):
        return f"El {self.nombre} puede volar sobre los {altura}m"

class Tiburon(Animal):
    def nadar(self, profundidad):
        return f"El {self.nombre} puede nadar hasta profundidades de {profundidad}m"

aguila1 = Aguila("aguila", 4)
print(aguila1.nombre)
print(aguila1.peso)
print(aguila1.descripcion())
print(aguila1.volar(100))

########################################

# Funciones para herencia
class Pokemon:
    def __init__(self, nombre, tipo):
        self.nombre = nombre
        self.tipo = tipo
    def descripcion(self):
        return f"Nombre: {self.nombre}, Tipo: {self.tipo}"

class Pikachu(Pokemon):
    def ataque(self, tipo_ataque):
        return f"El ataque de {self.nombre} es {tipo_ataque}"
    
pikachu = Pikachu("pokemon1", "Electrico")
print(pikachu.nombre)
print(pikachu.tipo)
print(pikachu.descripcion())
print(pikachu.ataque("Impactrueno"))

#isinstance(),se utiliza para determinar si un objeto es una instancia de una clase dada o de una de sus subclases
print("Pikachu es un pokemon?", "Si" if isinstance(pikachu, Pikachu) else "No")

#issubclass(), se utiliza para determinar si una clase es una subclase de otra clase dada
print("Pokemon es una subclase de la clase padre Pikachu?", "Si" if issubclass(Pokemon, Pikachu) else "No")

########################################

# super(), se utiliza para reutilizar el código existente en la clase padre y extenderlo o modificarlo en la clase hija
class Persona():
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def detalle_persona(self):
        print(f"El es {self.nombre} y tiene {self.edad}")
    
    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}"
class Empleado(Persona):
    def __init__(self, nombre, edad, sueldo):
        super().__init__(nombre, edad)
        self.sueldo = sueldo
    def detalle_persona(self):
        super().detalle_persona()
        print(f"Sueldo: {self.sueldo}")
    
    def __str__(self):
        return super().__str__() + f" y el sueldo es {self.sueldo}"
    
class Cliente(Persona):
    def __init__(self, nombre, edad, compra):
        Persona.__init__(self, nombre, edad)
        self.compra = compra
    def detalle_cliente(self):
        Persona.detalle_persona(self)
        print(f"Compra: {self.compra}")
empleado1 = Empleado("Juan", 19, 1100)
empleado1.detalle_persona()
cliente1 = Cliente("Alex", 19, 300)
cliente1.detalle_cliente()


# Herencia multiple
class A:
    def __init__(self):
        print("Soy clase A")
    def a(self):
        print("Soy metodo de A")

class B:
    def __init__(self):
        print("Soy clase B")
    def b(self):
        print("Soy metodo de B")

class C(B,A): #dara prioridad a la clase A y llamara  a su constructor
    def c(self):
        print("Soy metodo de C")

c = C()

