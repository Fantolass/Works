SomaNotas = 0
QuantidadeAlunos = 0

while True:
    NomeAluno = input("Digite o nome do aluno (ou 0 para sair): ")

    if NomeAluno == "0":
        break

    try:
        NotaAluno = float(input(f"Digite a nota de {NomeAluno}: "))
        SomaNotas += NotaAluno
        QuantidadeAlunos += 1
    except ValueError:
        print("Nota inválida. Por favor, digite uma nota válida em valores numéricos.")

MediaTurma = SomaNotas / QuantidadeAlunos
print(f"A média da turma é: {MediaTurma}")