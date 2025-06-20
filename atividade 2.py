print("Cadastre sua conta.")

while True:
    NomeUsuario = input("Digite o nome de usuário: ")
    SenhaUser = input("Digite sua senha: ")
    if SenhaUser == NomeUsuario:
        print("[ERRO]! A senha inserida não pode ser igual ao nome de usuário. Tente novamente!")
    else:
        print("Conta cadastrada com sucesso!")
        break