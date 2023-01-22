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
37
Andres
41
Morgana
39

output
Carlos
Fabiana
'''
n = int(input("El numero de alumnos es:"))
alumnos_notas = []
for i in range(n):
    nombre_alumno = input("Ingresa el nombre del alumno: ")
    nota_alumno = float(input(f"Ingresa la nota del alumno {nombre_alumno}: "))
    alumnos_notas.append([nombre_alumno, nota_alumno])

alumnos_notas.sort(key=lambda x: x[1])
nombres_estudiantes = []
nota_baja = alumnos_notas[0][1]
# 12 16 11 20 12
# 11 12 12 16 20
segunda_nota_baja = 0
for i in range(len(alumnos_notas)):
    if alumnos_notas[i][1] > nota_baja and segunda_nota_baja == 0:
        segunda_nota_baja = alumnos_notas[i][1]
        
    if segunda_nota_baja != 0 and alumnos_notas[i][1] == segunda_nota_baja:
        nombres_estudiantes.append(alumnos_notas[i][0])
        
nombres_estudiantes.sort()

for nombre_estudiante in nombres_estudiantes:
    print(nombre_estudiante)
