'''
Dados los nombres y calificaciones de cada estudiante en una clase de N estudiantes, guárdelos en una lista anidada e imprima los nombres de cualquier estudiante que tenga la segunda calificación más baja.

Nota: Si hay varios estudiantes con la segunda calificación más baja, ordene sus nombres alfabéticamente y escriba cada nombre en una nueva línea.

input
5
Fabiana
37.21
Carlos
37.21
Lucia
37.2
Andres
41
Morgana
39

output
Carlos
Fabiana
'''
alumno_nota = []
n = int(input("Ingrese el número de alumnos: "))

# Pedir el nombre y la nota de cada alumno
for _ in range(n):
    alumno_name = input("Ingrese el nombre del alumno: ")
    nota = float(input(f"Ingrese la nota del alumno {alumno_name}: "))
    alumno_nota.append([alumno_name, nota])

# Ordenar la lista por nota
alumno_nota.sort(key = lambda x:x[1])

nombres = []
# Obtener la nota más baja
nota_baja = alumno_nota[0][1]
segundan_baja = 0

#nota baja = 11
#notas 16, 11, 17, 12, 18, 12

# Recorrer la lista para encontrar la segunda nota más baja
for i in range(len(alumno_nota)):
    # Si la nota actual es mayor a la nota más baja y aún no se ha encontrado la segunda nota más baja
    if alumno_nota[i][1] > nota_baja and segundan_baja == 0:
        segundan_baja = alumno_nota[i][1]

    # Si se ha encontrado la segunda nota más baja y la nota actual es igual a ella
    if segundan_baja != 0 and alumno_nota[i][1] == segundan_baja:
        nombres.append(alumno_nota[i][0])
        print(nombres)

# Ordenar la lista de nombres
nombres.sort()

# Imprimir cada nombre de la lista
for alumno_name in nombres:
    print(alumno_name)