#ZEN DE PYTHON
# import this

#Comentarios, es lo que no se ejecuta y sirve para que otras personas entiendan tu codigo
# Esto es un comentario de una linea, puedes comentar una linea con los comandos ctrl + k + ctrl + c
# Tambien puedes comentarar varias lineas con esos comandos, solo tienes que seleccionar las lineas de codigo

'''
Este es un comentario multilinea
puedes descomentar "comentarios de una linea" con los comandos ctrl + k + ctrl + u
'''

#Variables

#Forma incorrecta
# !nombre = "Luciana"
# 1_var = 23

#Forma correcta
nombre_1 = "Valeria"
_var = 12.5

nombre_a = "doble comillas" 
nombre_b = 'comillas simples'
nombre_c = '''multinea
            esto
            es
            multilinea'''

#Funcion print, esta es una built-in function y sirve para imprimir mensajes por consola
# print(nombre_a)
# print(nombre_b)
# print(nombre_c)


#Otros argumentos de print()
print(nombre_a, end="mensaje final\n") #se agrega un str al final de lo que se imprima
print(nombre_a, nombre_b, sep="--") #separa los valores concatenados


#TIPOS DE DATOS

#Enteros(int)
entero1 = 12_000_000
entero2 = 12000000
entero3 = 31

#Reales(float)
real1 = 1.45
real2 = .4
real3 = 5.

#Cadenas(str)
cadena1 = "Hola"
cadena2 = 'a'
cadena3 = '''esto es tipo string'''

#Booleano(bool)
booleano1 = True
booleano2 = False

#OPERADORES

#Arimeticos
# print(2+3) #suma
# print(3*9) #producto
# print(5-1) #resta
# print(20/5) #división
# print(25%4) #modulo
# print(2**3) #potencia
# print(23//5) #división exacta

#Relacionales
# print(4>2) #Retorna True
# print(20<10) #Retorna False
# print(1_000==1000) #Retorna True
# print(5>=5) #Retorna True
# print(4<=6) #Retorna True
# print("Hola"!='Hola') #Retorna False

#Logícos
# print(4>2 and "b">"c") #Retorna False
# print("True" == True or 4 > 1) #Retorna True
# print(not 4 == "4") #Retorna True

#De pertenencia
# print(4 is 4) #Retorna True
# print("False" is not '''False''') #Retorna False

#De identidad
# print("a" in "alexandra") #Retorna True
# print(" " not in "Feliz Navidad") #Retorna False

#TYPE(), nos devuelve el tipo de dato de la variable
# print(type(entero1))
# print(type(real1))
# print(type(cadena1))
# print(type(booleano1))

#CASTEAR
cast1 = str(4)
cast2 = int("3")
cast3 = float(1_000)
cast4 = bool(1)



#CONCATENAR
# nombre = "Luisa"
# edad = 21
# print("Hola mi nombre es " + nombre + " y tengo "+ str(edad))
# print("Hola mi nombre es", nombre, "y tengo", str(edad))


#FORMATEO DE CADENAS
# print("Hola mi nombre es %s y tengo" % nombre, edad)
# print(f"Hola mi nombre es {nombre} y tengo {edad}")
# print("Hola mi nombre es {} y tengo {}".format(nombre, edad))
# print("Hola mi nombre es {1} y tengo {0}".format(edad, nombre))
# print("Hola mi nombre es {nombre} y tengo {edad}".format(nombre="Luisaa", edad=22))

#CARACTERES DE ESCAPE
# print("Lista de frutas:\n-Manzana\n-Sandia\n-Uva")
# print("Lista de frutas:\n\t-Manzana\n\t-Sandia\n\t-Uva")
# print("Luego dijo: \"Feliz navidad\"")

#ALGUNOS METODOS DE CADENAS
var_1 = "san luis gonzaga"
var_2 = "SAN LUIS GONZAGA"
var_3 = "san luis gonzaga"
var_4 = "Ingeniería de Sistemas"

#CAPITALIZE
var_1 = var_1.capitalize()
print(var_1) #San luis gonzaga

#LOWER
var_2 = var_2.lower()
print(var_2) #san luis gonzaga

#UPPER
var_3 = var_3.upper()
print(var_3) #SAN LUIS GONZAGA

#REPLACE
var_4 = var_4.replace("Sistemas", "Software") #Ingeníeria de Software



#INPUT
persona = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
dinero = float(input("Ingresa tu dinero: "))

print(f"Hola soy {persona}, tengo {edad} años y S/.{dinero} ")


#SENTENCIAS CONDICIONALES

#IF
edad_1 = int(input("Ingresa tu numero: "))
if edad_1 >= 18:
    print("Eres mayor de edad")

#IF-ELSE
if edad_1 >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

#IF-ELIF-ELSE
if edad_1 >= 40:
    print("Eres viejo")
elif edad_1 <=39 and edad_1 >= 20:
    print("Eres adulto")
elif edad_1 <=19 and edad_1 >= 16:
    print("Eres joven")
elif edad <= 15 and edad_1 >= 0:
    print("Eres un niño")
else:
    print("Edad invalida")

#ANIDADOS
if edad_1>=0 and edad_1<=100:
    if edad_1 >= 40:
        print("Eres viejo")
    elif edad_1 <=39 and edad_1 >= 20:
        print("Eres adulto")
    elif edad_1 <=19 and edad_1 >= 16:
        print("Eres joven")
    else:
        print("Eres un niño")
else:
    print("Edad invalida")

#OPERADOR TERNARIO, es un if else en una linea
dia = "soleado"
hacer = "Salir a jugar" if dia == "soleado" else "No salir a jugar"
print(hacer)

#NOTA: Cualquier valor que no sea false, None, 0 o una cadena vacía string ('')
# realmente retorna el valor true cuando es probada como una declaración condicional, 
# por lo tanto puedes simplemente usar el nombre de una variable para probar si es true, 
# o si al menos existe

mensaje = "Hola"
if mensaje:
    print(f"El mensaje es {mensaje}")
    
#NOTA: En Python las variables son "etiquetas" que permiten hacer referencia a los datos 
# (que se guardan en unas "cajas" llamadas objetos).

#ID() -> La función devuelve una identificación única para el objeto especificado.

personas = ["Laura", "Jose", "sofia"]
personas2 = personas
personas3 = personas[:]
# print(personas)
# print(personas2)
# print(personas3)
# print(id(personas))
# print(id(personas2))
# print(id(personas3))


#NOTA: CASE-SENSITIVE, si diferencia entre mayusculas y minusculas
a = 12
A = 13
if a == A:
    print("Son iguales")


