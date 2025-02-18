from cli.auth import Auth

class CommandLine:
    def start(self):
        print("Bem vindo ao Tassio Libraries")
        auth = Auth()
        if auth.start():
            print("Bem vindo ao Tassio Libraries")
            while True:
                opcao: str = self.input_opcao()
        print("Programa finalizado!")

    def input_opcao(self) -> str:
        print("1 - Pesquisar")
        print("2 - Cadastrar")
        print("3 - Sair\n")
        return input()


