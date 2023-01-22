'''
Se debe encontrar el puntaje n del subcampeón del torneo de ajedrez. Guárdalos en una lista y encuentra la puntuación del subcampeón.

input:
6
2 3 5 6 6 7

output
6
'''

# n = int(input("Ingresa el numero de participantes: "))
# arr = list(set(map(int, input("ingresa los puntajes separados por espacios: ").split())))
# arr.sort(reverse=True)
# print(arr[1])

try:
    n = int(input("Ingresa el numero de participantes: "))
    if n <= 0:
        raise ValueError("El numero de participantes debe ser mayor a 0")
    arr = list(set(map(int, input("ingresa los puntajes separados por espacios: ").split())))
    if len(arr) != n:
        raise ValueError("El numero de puntajes ingresados no coinciden con el de participantes")
    arr = list(set(arr))
    arr.sort(reverse=True)
    if len(arr) < 2:
        raise ValueError("No hay suficientes puntajes para determinar un subcampeon")
    print("El puntaje del subcampeon es: ", arr[1])
except ValueError as e:
    print(f"Error: {e}")