alunos = ["Lucas", "Mariana", "Pedro", "Sofia", "Thiago"]
notas = [8.5, 5.0, 6.0, 9.2, 4.8]

for i in range(len(alunos)):
    situacao = "Aprovado" if notas[i] >= 6.0 else "Reprovado"
    print(f"Aluno: {alunos[i]} | Nota: {notas[i]:.1f} | Situação: {situacao}")