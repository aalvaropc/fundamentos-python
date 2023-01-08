# WHILE -> se utiliza para crear un bucle que se ejecuta mientras se cumpla una condición específica

num = 0
while num<=10:
    print(num)
    num = num + 1 # contador


# FOR -> se utiliza para iterar sobre una secuencia
for i in range(11):
    print(i)


dias_semana = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]
for i in dias_semana:
    print(i)

# break -> se utiliza para terminar un bucle
password = '12345'
while True:
    entrada = input("Ingresa tu contraseña: ")
    if entrada == password:
        print("Bienvenido ..")
        break
    print("Contraseña invalida")

# pass -> se utiliza como una declaración nula, principalmente cuando se necesita una declaración syntácticamente válida pero no se quiere ningún código que se ejecute
for n in range(2, 10):
    if n % 2 == 0:
        pass  # La división por 2 es irrelevante, así que se pasa
    else:
        print(f'{n} es un número impar')

# continue -> se utiliza para saltar a la siguiente iteración de un bucle
for n in range(2, 10):
    if n % 2 == 0:
        continue  # Salta a la siguiente iteración
    print(f'{n} es un número impar')


# for-else
numbers = [9, 8, 7, 6, 5]
numbers = []
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for n in numbers:
    print(n)
    if n == 5:
        break
else:
    print("Última iteración") # Se ejecutara en la última iteración

# enumerate -> sirve para iterar sobre secuencias y obtener el índice de cada elemento junto con el elemento
nombres = ["Juan", "Ana", "Luis"]
for i, nombre in enumerate(nombres):
    print(f"{i}: {nombre}")

# Bucles anidados

# Bucle anidado para iterar sobre dos listas al mismo tiempo
lista_1 = [1, 2, 3]
lista_2 = ['a', 'b', 'c']
for x in lista_1:
    for y in lista_2:
        print(f'{x}, {y}')

# Bucle anidado para imprimir una tabla de multiplicar
for i in range(1, 11):
    for j in range(1, 11):
        print(f'{i} x {j} = {i * j}')        

# Acumulador vs Contador
# acumulador -> es una variable que se utiliza para ir sumando (o restando) los valores que se van procesando en un ciclo.
total = 0
for i in range(5):
    total += i
print(total)  # Imprime: 10

# contador -> es una variable que se utiliza para llevar un registro de cuántas veces ha sucedido un evento o ha sido cumplida una condición en un ciclo

count = 0
for i in range(5):
    if i % 2 == 0:
        count += 1
print(count)  # Imprime: 3