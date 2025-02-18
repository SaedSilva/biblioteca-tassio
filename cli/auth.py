from domain.services.auth_service import AuthService


class Auth:
    def __init__(self, auth_service: AuthService = AuthService()):
        self.auth_service = auth_service

    def start(self) -> bool:
        while True:
            print("1 - Entrar / Login")
            print("2 - Sair")
            opcao = input()
            if opcao == "1":
                return self.login()
            elif opcao == "2":
                return False
            else:
                print("Opção inválida! Tente novamente.")

    def login(self) -> bool:
        while True:
            usuario = input("Digite seu usuário: \n")
            senha = input("Digite sua senha: \n")
            if self.auth_service.authenticate(usuario, senha):
                print("Logado com sucesso!")
                return True
            else:
                print("Usuário ou senha inválidos!")

    def signup(self) -> bool:
        print("Faça seu cadastro!")
        while True:
            nome = input("Digite seu nome: \n")
            if len(nome) < 3:
                print("Nome precisa ter ao menos 3 caracteres!")
                continue
            usuario = input("Digite seu usuário: \n")
            if len(usuario) < 3:
                print("Usuário precisa ter ao menos 3 caracteres!")
                continue
            senha = input("Digite sua senha: \n")
            if len(senha) < 6:
                print("Senha precisa ter ao menos 6 caracteres!")
                continue
            if self.auth_service.signup(nome, usuario, senha):
                print("Cadastro realizado com sucesso!")
                return True
            else:
                print("Usuário já cadastrado!")
