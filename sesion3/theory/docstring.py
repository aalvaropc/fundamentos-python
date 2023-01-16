# DOCSTRING
'''
Son cadenas de documentación que se encuentran al principio de un módulo, función, clase o método. Estas cadenas proporcionan información sobre lo que hace el código y cómo utilizarlo. 
'''

'''
Definir una funcion cus_max() que tome como argumentos dos numeros y devuelva el mayor
'''
def cus_max(num1: int, num2: int) -> int:
    """Dados dos números de entrada retornar el maximo de ambos

    Args:
        num1 (int): Primer número a comparar
        num2 (int): Segundo número a comparar

    Returns:
        int: Mayor de ambos
    """        
    if num1 > num2:
        return num1
    else:
        return num2
maximo = cus_max(10,10)
print('maximo: ', maximo)

# print(cus_max.__doc__)


