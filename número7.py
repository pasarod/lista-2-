numeros = []
for i in range(8):
    valor = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(valor)

busca = int(input("Digite um número para pesquisar: "))
encontrado = False

for num in numeros:
    if num == busca:
        encontrado = True
        break

if encontrado:
    print(f"O número {busca} está na lista.")
else:
    print(f"O número {busca} não foi encontrado na lista.")