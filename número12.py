numeros = [2, 5, 2, 8, 5, 9, 2, 8, 10]
sem_repeticao = []

for num in numeros:
    ja_existe = False
    for item in sem_repeticao:
        if item == num:
            ja_existe = True
            break
    if not ja_existe:
        sem_repeticao.append(num)

print("Lista original:", numeros)
print("Sem repetição:", sem_repeticao)