'''
13- Una tienda de ropa ha establecido los porcentajes de descuento que se indican a continuación de acuerdo con ciertas características
del comprador: nacionalidad (1,2) y del producto que compra: sexo(H,M), talla(Niño, Joven, Adulto). Se sabe que una persona puede comprar varios productos por lo que se desea mostrar como resultados lo siguiente: nombre del comprador, cantidad de productos comprados, importe comprado, importe descontado y el importe a pagar, para lo cual se deben ingresar los datos que sean necesarios
			  Niño(sexo)	Joven(sexo) Adulto(sexo)
Nacionalidad	 H – M       H – M        H - M
	1		     5 – 4	     7 – 9	      10 - 12
	2			 4 – 5       9 – 7	      12 - 10
'''
while True:
    nacionalidad = int(input("Ingrese la nacionalidad (1/2): "))
    if nacionalidad == 1 or nacionalidad == 2:
        break
    print("Error, ingrese una nacionalidad valida")
while True:
    sexo = input("Ingrese su sexo (M/F): ").upper()
    if sexo == "M" or sexo == "F":
        break
    print("Error, ingrese un sexo valido")  
while True:
    talla = input("Ingrese su talla (Niño/Joven/Adulto): ").capitalize()  
    if talla == "Niño" or talla == "Joven" or talla == "Adulto":
        break
    print("Error, ingrese un talla valido")
while True:
    nombre = input("Ingrese su nombre: ").capatilize()
    if nombre != "":
        break
    print("Error, ingrese un nombre")
while True:
    producto_precio = float(input("Ingrese el precio del producto: "))
    if producto_precio > 0:
        break
    print("Error, ingrese un precio deproducto valido")
while True:
    cantidad_producto = int(input("Ingrese la cantidad de productos: "))
    if cantidad_producto > 0:
        break
    print("Error, ingrese una cantidad de productos valida")

impc = cantidad_producto * producto_precio

if nacionalidad == 0:
    var = 1 if sexo == "M" else 2
else:
    var = 3 if sexo == "M" else 4

match talla:
    case 'Niño':
        match var:
            case 1: impd = impc * 0.05
            case 2: impd = impc * 0.04
            case 3: impd = impc * 0.04
            case _: impd = impc * 0.05
    case "Joven":
        match var:
            case 1: impd = impc * 0.07
            case 2: impd = impc * 0.09
            case 3: impd = impc * 0.09
            case _: impd = impc * 0.07
    case _:
        match var:
            case 1: impd = impc * 0.1
            case 2: impd = impc * 0.12
            case 3: impd = impc * 0.12
            case _: impd = impc * 0.1

impp = impc - impd
print(f"""BOLETA DE COMPRA
      Cantidad: {cantidad_producto}
      Importe comprado: {round(impc, 2)}
      Importe Descontado: {round(impd, 2)}
      Importe a pagar: {round(impp, 2)} 
      """)
    
