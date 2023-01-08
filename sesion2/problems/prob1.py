# Obtener los números primos en un intervalo de números
primos = []
for n in range(2, 100):
    for x in range(2, n):
        if n % x == 0:
            break
    else:
        primos.append(n)
print(f'primos: {primos}')