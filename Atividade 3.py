SomaPeso = 0
SomaAltura = 0
QuantidadeCliente = 0

#Extremos
MaisAlto = 0
MatriculaMaisAlto = 0

MaisBaixo = float('inf')
MatriculaMaisBaixo = 0

MaisGordo = 0
MatriculaMaisGordo = 0

MaisMagro = float("inf")
MatriculaMaisMagro = 0

#Perguntas

while True:
    try:
        MatriculaCliente = int(input("Informe a sua matrícula (ou 0 para sair): "))
    except ValueError:
        print("Matrícula inválida. Por favor, insira um valor inteiro.")
        continue
    if MatriculaCliente == 0:
        break

    try:
        PesoCliente = float(input(f"Digite o peso do portador da matrícula {MatriculaCliente}: "))
        AlturaCliente = float(input(f"Digite a altura do portador da matrícula {MatriculaCliente}: "))
        SomaPeso += PesoCliente
        SomaAltura += AlturaCliente
        QuantidadeCliente += 1
        #Mais alto
        if AlturaCliente > MaisAlto:
            MaisAlto = AlturaCliente
            MatriculaMaisAlto = MatriculaCliente
        #Mais baixo
        if AlturaCliente < MaisBaixo:
            MaisBaixo = AlturaCliente
            MatriculaMaisBaixo = MatriculaCliente
        #Mais gordo
        if PesoCliente > MaisGordo:
            MaisGordo = PesoCliente
            MatriculaMaisGordo = MatriculaCliente
        #Mais magro
        if PesoCliente < MaisMagro:
            MaisMagro = PesoCliente
            MatriculaMaisMagro = MatriculaCliente

    except ValueError:
        print("Valor inválida, por favor por favor informe o peso e a altura em valores numéricos.")

#Resultados

if QuantidadeCliente > 0:
    MediaAltura = SomaAltura / QuantidadeCliente
    MediaPeso = SomaPeso / QuantidadeCliente
    print(f"A média de peso dos clientes da academia é: {MediaPeso:.2f} kg")
    print(f"A média de altura dos clientes da academia é: {MediaAltura:.2f} m")

    print(f"Cliente mais alto: matrícula {MatriculaMaisAlto}, altura {MaisAlto:.2f} m")
    print(f"Cliente mais baixo: matrícula {MatriculaMaisBaixo}, altura {MaisBaixo:.2f} m")
    print(f"Cliente mais gordo: matrícula {MatriculaMaisGordo}, peso {MaisGordo:.2f} kg")
    print(f"Cliente mais magro: matrícula {MatriculaMaisMagro}, peso {MaisMagro:.2f} kg")
else:
    print("Nenhum dado válido foi inserido.")