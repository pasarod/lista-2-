numeros = [15, 42, 8, 42, 23, 19, 37]

maior = None
segundo_maior = None

for num in numeros:
    if maior is None or num > maior:
        segundo_maior = maior
        maior = num
    elif num != maior and (segundo_maior is None or num > segundo_maior):
        segundo_maior = num

print("Lista:", numeros)
print("Segundo maior valor distinto:", segundo_maior)