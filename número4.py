notas = [7.5, 8.0, 6.0, 9.5, 5.5]
soma = 0
quantidade = 0

for nota in notas:
    soma += nota
    quantidade += 1

media = soma / quantidade
print(f"Média final: {media:.2f}")