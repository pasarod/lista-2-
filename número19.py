produtos = ["Teclado", "Mouse", "Monitor", "Notebook", "Headset"]
quantidades = [12, 25, 4, 3, 8]

# 1. Consultar um produto
busca = input("Digite o nome do produto para consultar: ")
indice_encontrado = -1

for i in range(len(produtos)):
    if produtos[i].lower() == busca.lower():
        indice_encontrado = i
        break

if indice_encontrado != -1:
    print(f"Produto: {produtos[indice_encontrado]} | Quantidade atual: {quantidades[indice_encontrado]}")
    
    # 2. Alterar sua quantidade
    nova_qtd = int(input("Digite a nova quantidade em estoque: "))
    quantidades[indice_encontrado] = nova_qtd
    print("Estoque atualizado com sucesso!")
else:
    print("Produto não encontrado no cadastro.")

# 3. Listar produtos com estoque inferior a 5 unidades
print("\nProdutos com estoque crítico (menos de 5 unidades):")
for i in range(len(produtos)):
    if quantidades[i] < 5:
        print(f"- {produtos[i]}: {quantidades[i]} unidades")

# 4. Produto com maior quantidade em estoque
indice_maior = 0
for i in range(1, len(quantidades)):
    if quantidades[i] > quantidades[indice_maior]:
        indice_maior = i

print(f"\nProduto com maior estoque: {produtos[indice_maior]} ({quantidades[indice_maior]} unidades)")