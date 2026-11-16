numeros = [34, 12, 89, 3, 56, 21, 90, 7]

maior = numeros[0]
menor = numeros[0]

for num in numeros:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior valor:", maior)
print("Menor valor:", menor)