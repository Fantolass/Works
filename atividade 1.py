nota = int(input("Digite uma nota de 1 a 10: "))

while nota <= 0 or nota > 10:
    print("Nota inválida.")
    nota = int(input("[ERRO]! Digite novamente uma nota entre 1 e 10: "))
if nota >= 1 or nota <= 10:
    print(f"Sua nota '{nota}' é válida, parabéns!")