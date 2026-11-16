nomes = ["Ana", "Bruno", "Carlos", "Daniel", "Eduarda"]
busca = input("Digite um nome para pesquisar: ")

posicao = -1
for i in range(len(nomes)):
    if nomes[i].lower() == busca.lower():
        posicao = i
        break

if posicao != -1:
    print(f"O nome '{nomes[posicao]}' aparece no índice {posicao} (posição {posicao + 1}).")
else:
    print("Nome não encontrado.")