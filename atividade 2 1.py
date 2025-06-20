import re
print("Cadastre sua conta.")

def SenhaValida(SenhaUsuario, NomeUsuario):
    if SenhaUsuario == NomeUsuario:
        print("[ERRO]! A senha não pode ser igual ao nome de usuário. Tente novamente!")
        return False
    if len(SenhaUsuario) < 8:
        print("[ERRO]! A senha deve ter pelo menos 8 caracteres. Tente novamente!")
        return False
    if not re.search(r"[A-Za-z]", SenhaUsuario):
        print("[ERRO]! A senha deve ter pelo menos uma letra. Tente novamente!")
        return False
    if not re.search(r"[0-9]", SenhaUsuario):
        print("[ERRO]! A senha deve ter pelo menos um número. Tente novamente!")
        return False
    if not re.search(r"[!@#$%¨&*()_-+.,]", SenhaUsuario):
        print("[ERRO]! A senha deve ter pelo menos um caractere especial. Tente novamente!")
        return False
    return True

NomeUsuario = input("Digite seu nome de usuário: ")

while True:
    SenhaUsuario = input("Digite sua senha: ")
    if SenhaValida(SenhaUsuario, NomeUsuario):
        print("Cadastro realizado com sucesso!")
        break