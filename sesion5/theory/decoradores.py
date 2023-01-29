'''
son funciones especiales que se utilizan para modificar la funcionalidad de otras funciones o métodos. Los decoradores se utilizan para aplicar comportamientos adicionales a una función o método sin tener que modificar su código original
'''
def mi_decorador(funcion):
    def envoltorio():
        print("Antes de ejecutar la función")
        funcion()
        print("Después de ejecutar la función")
    return envoltorio

@mi_decorador
def mi_funcion():
    print("Ejecutando mi función")

mi_funcion()


# Classes como decoradores
class MiDecorador:
    def __init__(self, funcion):
        self.funcion = funcion

    def __call__(self): #call se utiliza para convertir una clase a una funcion llamanda 
        print("Antes de ejecutar la función")
        resultado = self.funcion()
        print("Después de ejecutar la función")
        return resultado

@MiDecorador
def mi_funcion():
    print("Ejecutando mi función")

mi_funcion()