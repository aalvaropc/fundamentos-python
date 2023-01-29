"""
Se refiere a la ocultación de los detalles de implementación de un objeto o una clase detrás de una interfaz pública.
Esto permite que los detalles internos de la implementación sean modificados sin afectar al comportamiento externo del objeto o la clase
"""
class Auto:
    __marca = "Toyota"
    __modelo = "2020"
    def __init__(self, marca, modelo):
        self.__marca = marca
        self.__modelo = modelo
    def __metodo_privado(self):
        return "Soy un metodo privado"
    #Crear get y set
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    
    def set_marca(self, marca):
        self.__marca = marca
        
    def set_modelo(self, modelo):
        self.__modelo = modelo
    
    
    def __str__(self):
        return f"La marca del auto es {self.__marca}"

auto1 = Auto("Toyota", "2020")
print(auto1.get_marca())
auto1.set_marca("Honda")
print(auto1)