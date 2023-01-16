task = []
while True:
    user_action = input("TODO\nEscribe agregar, mostrar, editar, completar, salir: ")
    user_action = user_action.strip()

    match user_action:
        case user_action if user_action.startswith('agregar'):
            todo = user_action[8:]
            task.append(f"{len(task)+1}- {todo}")
            print("Tarea agregada")
        case user_action if user_action.startswith('mostrar'):
            for i in range(len(task)):
                print(f"{task[i]}")
        case user_action if user_action.startswith('editar'):
            todo = user_action[7:]
            nueva_tarea = input("Escribe la nueva tarea: ")
            task[int(todo)-1] = f"{todo}- {nueva_tarea}"
            print("Tarea editada")
        case user_action if user_action.startswith('completar'):
            number = int(user_action[10:])
            task.pop(number-1)
            print("La tarea fue removida")
            x = 0
            for i in task:
                tarea = i[2:]
                task[x] = f"{x+1}- {tarea}"
                x += 1
        case user_action if user_action.startswith('salir'):
            break
        case _:
            print("Comando invalido")
print("Chau..")