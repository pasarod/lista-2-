vendas = [1250, 980, 1430, 2100, 1750, 890, 1620]

total_vendido = 0
maior_venda = vendas[0]
menor_venda = vendas[0]

for valor in vendas:
    total_vendido += valor
    if valor > maior_venda:
        maior_venda = valor
    if valor < menor_venda:
        menor_venda = valor

media_diaria = total_vendido / len(vendas)

dias_acima_media = 0
for valor in vendas:
    if valor > media_diaria:
        dias_acima_media += 1

percentual_acima = (dias_acima_media / len(vendas)) * 100

print(f"Total vendido na semana: R$ {total_vendido:.2f}")
print(f"Média diária de vendas: R$ {media_diaria:.2f}")
print(f"Maior venda: R$ {maior_venda:.2f}")
print(f"Menor venda: R$ {menor_venda:.2f}")
print(f"Dias acima da média: {dias_acima_media} dias")
print(f"Percentual de dias acima da média: {percentual_acima:.2f}%")