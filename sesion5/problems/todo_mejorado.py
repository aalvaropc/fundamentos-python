import time
import functions

while True:
    #Se imprime la fecha actual
    now = time.strftime("%b %d, %Y %H:%M:%S")
    print(now)
    
    user_action = input("TODO\nEscribe agregar, mostrar, editar, completar, salir: ")
    user_action = user_action.strip()

    match user_action:
        case user_action if user_action.startswith('agregar'):
            
            todo = user_action[8:]

            todos = functions.get_todos()

            todos.append(todo + "\n")
            
            functions.write_todos(todos)
            
            print("Tarea agregada")

        case user_action if user_action.startswith('mostrar'):
            
            todos = functions.get_todos()
            
            for index, item in enumerate(todos):
                item = item.strip('\n')
                fila = f"{index + 1}- {item}"
                print(fila)
        
        case user_action if user_action.startswith('editar'):
            try:
                number = int(user_action[7:])
                print(f"Tarea seleccionada {number}")

                number = number - 1
                
                todos = functions.get_todos()
                
                new_todo = input("Ingresa la nueva tarea: ")
                todos[number] = new_todo + '\n' 

                functions.write_todos(todos)
                print("Tarea editada")
            except ValueError:
                print("Comando invalido")
                continue
        case user_action if user_action.startswith('completar'):
            try:
                number = int(user_action[10:])

                todos = functions.get_todos()
                index = number - 1
                todo_to_remove = todos[index].strip("\n")
                todos.pop(index)

                functions.write_todos(todos)
                print("La tarea fue completada")
            except IndexError:
                print("No hay una tarea con ese número de orden")
                continue
        case user_action if user_action.startswith('salir'):
            break
        case _:
            print("Comando invalido")
    print("\n")
print("Chau..")