'''
Se debe encontrar el puntaje n del subcampeón del torneo de ajedrez. Guárdalos en una lista y encuentra la puntuación del subcampeón.

input:
6
2 3 5 6 7 7

output
8
'''

while True:
    try:
        n = int(input("Ingrese n: "))
        if n<=0:
            raise ValueError("n debe ser mayor a 0")

    except ValueError as e:
        print(e)
        
    else:
        break

lista_puntajes = input("Ingrese los puntajes:").split()
lista_puntajes = map(int, lista_puntajes)
print(sorted(set(lista_puntajes), reverse=True)[1])






# students_grade = []
# if __name__ == '__main__':
#     for _ in range(int(input("Ingresa el numero de veces: "))):
#         name = input("Ingresa el nombre: ")
#         score = float(input("Ingrese el marcador: "))
#         students_grade.append([name, score])
#     sorted_scores = sorted(list(set([x[1] for x in students_grade])))
#     second_lowest = sorted_scores[1]
#     low_final_list = []
#     for student in students_grade:
#         if second_lowest == student[1]:
#             low_final_list.append(student[0])
#     for student in sorted(low_final_list):
#         print(student)

