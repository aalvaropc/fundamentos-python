#PROBLEMA1
# x = float(input("Ingresa la x: "))
# y = 1/(x+(1/(x+1/(x+1/x))))
# print(round(y,2))

#PROBLEMA2
# num1 = int(input("Ingresa el primer numero: "))
# num2 = int(input("Ingresa el segundo numero: "))
# num3 = int(input("Ingresa el tercer numero: "))

# print(f"El numero mayor es: {max(num1, num2, num3)}")
# print(f"El numero menor es: {min(num1, num2, num3)}")

#PROBLEMA3
# f = int(input("Ingrese los grados farenheit: "))
# c = (f-32)*(5/9)
# print("Los grados celsious son: {}".format(round(c,2)))

#PROBLEMA4
# base = float(input("Ingresa la base: "))
# altura = float(input("Ingresa la altura: "))
# if(base>0 and altura>0):
#     perimetro = 2*altura+2*base
#     area = base * perimetro
#     print(f"El area del rectangulo es {area}")
#     print(f"EL perimetro del rectangulo es {perimetro}")
# else:
#     print("Datos invalidos ingresados")

#PROBLEMA5

# prestamo = float(input("Ingrese el prestamo: "))
# if(prestamo>200):
#     totalPagar = prestamo + prestamo * 0.03
#     print(f"El total a pagar mas el interes es: {totalPagar}")
# else:
#     print("El prestamo debe ser mayor a S/.200")

#PROBLEMA6
# print("PRENDAS\nCamisa\nPantalones\nZapatos\nRopaInterior")
# tipoPrenda = input("Ingrese el tipo de prenda: ")
# cantidad = int(input("Ingresa la cantidad"))
# descuento = 0

# if((tipoPrenda=="Camisa" or tipoPrenda=="Pantalones" or tipoPrenda=="Zapatos" or tipoPrenda=="RopaInterior") and cantidad>0):
#     if(tipoPrenda == "Camisa"):
#         montoPagar = cantidad * 100
#     elif(tipoPrenda == "Pantalones"):
#         montoPagar = cantidad * 150
#     elif(tipoPrenda == "Zapatos"):
#         montoPagar = cantidad * 190
#     elif(tipoPrenda == "RopaInterior"):
#         montoPagar = cantidad * 40
        
#     valorArticulo = montoPagar
#     if(cantidad == 3 and(tipoPrenda == "Camisa" or tipoPrenda == "Pantalon")):
#         montoPagar = montoPagar - montoPagar * 0.10
#         descuento = montoPagar * 0.10

#     if(cantidad == 3 and(tipoPrenda == "Zapatos")):
#         montoPagar = montoPagar - montoPagar * 0.30
#         descuento = montoPagar * 0.30

#     print(f"El valor del articulo es: {valorArticulo}\nDescuento obtenido: {descuento}\nValor total a pagar {montoPagar}")
# else:
#     print("Datos invalidos")

#PROBLEMA7
# clave = input("Ingrese la clave: ")
# dineroBase = float(input("Ingrese el dinero base en dolares: "))
# opcion = int(input("1. Retiro de dinero\n2. Deposito de dinero\n3. Cambio de clave\n4. Finalizar\n->"))

# if(opcion == 1):
#     tipomoneda = input("dolares o soles: ")
#     montoRetirar = float(input("Ingrese el monto a retirar: "))
#     if((montoRetirar<=dineroBase and tipomoneda=="dolares") or (montoRetirar*3.85<=dineroBase and tipomoneda=="soles")):
#         if(tipomoneda == "soles"):
#             montoRetirar = montoRetirar * 3.85
        
#         dineroBase = dineroBase - montoRetirar    
#         print(f"El retiro es de {montoRetirar} y el dinero actual es {dineroBase} $")

#     else:
#         print("No cuentas con suficiente saldo")
# elif(opcion == 2):
#     tipomoneda = input("dolares o soles: ")
#     montoDepositar = float(input("Ingrese el monto a depositar: "))
#     if(tipomoneda == "soles"):
#         montoDepositar = montoDepositar/3.85
#     dineroBase = dineroBase + montoDepositar

#     print(f"El deposito es de {montoDepositar} y el dinero actual es {dineroBase} $")
# elif(opcion==3):
#     clavePrueba = input("Ingrese la clave:")
#     if(clavePrueba == clave):
#         nuevaClase = input("Ingresa la nueva clave: ")
#         clave = nuevaClase
#         print("La clave fue cambiada con exito")
#     else:
#         print("Clave incorrecta")
# elif(opcion==4):
#     print("Gracias por usar BankApp, vuelva pronto")
# else:
#     print("La opcion ingresada es invalida")


