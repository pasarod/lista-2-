numeros = []
soma = 0.0

for i in range(10):
    num = float(input(f"Digite o {i + 1}º número real: "))
    numeros.append(num)
    soma += num

media = soma / len(numeros)
print(f"\nMédia calculada: {media:.2f}")
print("Valores acima da média:")

for num in numeros:
    if num > media:
        print(num)