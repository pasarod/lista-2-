numeros = []

for i in range(5):
    num = int(input(f"Digite o {i + 1}º número: "))
    numeros.append(num)

print("Lista antes da remoção:", numeros)

remover = int(input("Digite o número que deseja remover: "))

if remover in numeros:
    numeros.remove(remover)
    print("Lista depois da remoção:", numeros)
else:
    print("Número não encontrado na lista. Lista inalterada:", numeros)