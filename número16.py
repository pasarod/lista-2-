matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

soma_total = 0

print("Elementos da matriz:")
for i in range(len(matriz)):
    soma_linha = 0
    for j in range(len(matriz[i])):
        valor = matriz[i][j]
        print(valor, end=" ")
        soma_linha += valor
        soma_total += valor
    print(f" -> Soma da linha {i + 1}: {soma_linha}")

print("\nSoma de todos os valores:", soma_total)