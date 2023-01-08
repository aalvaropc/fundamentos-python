# Hallar el MCD de dos números
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

mcd = 0

menor = min(num1, num2)

for i in range(menor, 0, -1):
    if num1 % i == 0 and num2 % i == 0:
        mcd = i
        break

if mcd == 0:
    mcd = menor

print(f"El MCD de {num1} y {num2} es {mcd}")