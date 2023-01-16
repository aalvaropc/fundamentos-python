# RECURSIVIDAD
'''
Es una técnica de programación en la cual una función se llama a sí misma de manera repetida hasta que se alcanza un caso base. 
El caso base es una condición específica en la cual la función deja de llamarse a sí misma y devuelve un resultado
'''
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)



# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34 ...
def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(3))
#fibo2 + fibo1 -> fibo1 + fibo0 + fibo1 -> 1 + 0 + 1