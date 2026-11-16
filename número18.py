numeros = [2, 3, 2, 5, 3, 2]
visitados = []

for i in range(len(numeros)):
    atual = numeros[i]
    
    
    ja_contado = False
    for v in visitados:
        if v == atual:
            ja_contado = True
            break
            
    if not ja_contado:
        visitados.append(atual)
        contagem = 0
        for num in numeros:
            if num == atual:
                contagem += 1
        vez = "vez" if contagem == 1 else "vezes"
        print(f"{atual} aparece {contagem} {vez}")