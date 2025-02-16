from domain.services.auth_service import AuthService


class Auth:
    def __init__(self):
        self.logged = False

    def start(self) -> bool:
        opcao = input("Digite 1 para login e 2 para cadastro: \n")
        if opcao == "1":
            return self.login()
        elif opcao == "2":
            return self.signup()
        else:
            print("Opção inválida!")
            return False

    def login(self) -> bool:
        auth_service = AuthService()
        while True:
            usuario = input("Digite seu usuário: \n")
            senha = input("Digite sua senha: \n")
            if auth_service.authenticate(usuario, senha):
                self.logged = True
                print("Logado com sucesso!")
                return True
            else:
                print("Usuário ou senha inválidos!")

    def signup(self) -> bool:
        login_service = AuthService()
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
            if login_service.signup(nome, usuario, senha):
                print("Cadastro realizado com sucesso!")
                self.logged = True
                return True
            else:
                print("Usuário já cadastrado!")
