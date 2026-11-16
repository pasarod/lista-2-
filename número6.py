numeros = [11, 22, 33, 44, 55, 66, 77, 88, 99, 100]
pares = 0
impares = 0

for num in numeros:
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1

print("Quantidade de pares:", pares)
print("Quantidade de ímpares:", impares)