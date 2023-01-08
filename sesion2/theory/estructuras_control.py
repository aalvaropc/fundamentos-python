#ESTRUCTURA DE CONTROL DE FLUJO CONDICIONAL

#IF, ELIF Y ELSE(SESION1)
# OPERADORES TERNARIOS

numero = 14
mensaje = "Es par" if numero %2 == 0 else "Es impar" 
print(mensaje)

#OPERADORES TERNARIOS ANIDADOS
x = 90
y = 90
resultado = f"{x} es mayor que {y}" if x > y else f"{x} es menor que {y}" if x < y else "son iguales"
print(resultado)

#OTROCASO
condicion = 11
# variable = (falso, verdad)[condicion]
resultado = ("Desaprobo el curso", "Aprobo el curso")[condicion>10]
print(resultado)

#OTRO CASO Y PORQUE NO ES TAN BUENO
# condicion = True
# resultado = (1/0, 2)[condicion]
# print(resultado) #NO USARLO POR QUE EVALUA LAS DOS CONDICIONES EN ESTE CASO DEVUELVE UN ERROR




#Structural Pattern Matching

# basico
status = 34534634
match status:
        case 400:
            print("Bad request")
        case 401:
            print("Unauthorized")
        case 403:
            print("Forbidden")
        case 404:
            print("Not found")
        case _:
            print("Unknown error")

#casos combinados
match status:
        case 400:
            print("Bad request")
        case 401 | 403:
            print("Authentication error")
        case 404:
            print("Not found")
        case _:
            print("Other error")

#usando if
edad = 20
match edad:
    case edad if edad >= 0 and edad <=1: print("Neonatal")
    case edad if edad >= 2 and edad <=14: print("Infancia")
    case edad if edad >= 15 and edad <=17: print("Adolescencia")
    case edad if edad >= 18 and edad <=34: print("Adultos Jovenes")
    case edad if edad >= 35 and edad <=64: print("Madurez")
    case edad if edad >= 65 and edad <=115: print("Tercera edad")
    case _: print("Edad invalida")

#otro caso
item = ["Noches", "Leer un libro", "Salir a pasear"]

match item:
        case [time, action]:
            print(f'Buenos {time}! Es tiempo de {action}!')
        case [time, *actions]:
            print(f'Buenos {time}!')
            for action in actions:
                print(f'Es tiempo de {action}!')

#patrones anidados

points = [(0, 1), (0, 2)]
match points:
    case []:
        print("No hay puntos en la lista")
    case [(0, 0)]:
        print("El origen es el unico punto en la lista")
    case [(x, y)]:
        print(f"Un solo punto {x=}, {y=} esta en la lista")
    case [(0, y1), (0, y2)]:
        print(f"Do puntos en el eje Y y en {y1=}, {y2=} estan en la lista")
    case _:
        print("Algo más se encuentra en la lista")

