from cli.auth import Auth
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository
from domain.repositories.sqlite_helper import SQLiteHelper
from domain.services.auth_service import AuthService
from domain.services.customer_service import CustomerService


class CommandLine:
    def start(self):
        sqlite_helper = SQLiteHelper()
        employee_repository = EmployeeRepository(sqlite_helper)
        auth_service = AuthService(employee_repository)
        auth_cli = Auth(auth_service)

        print("Bem vindo ao Tassio Libraries")
        if auth_cli.start():
            customer_repository = CustomerRepository(sqlite_helper)
            customer_service = CustomerService(customer_repository)
            print("Bem vindo ao Tassio Libraries")
            while True:
                opcao: str = self.input_opcao()

        print("Programa finalizado!")

    def input_opcao(self) -> str:
        while True:
            print("1 - Pesquisar Livros")
            print("2 - Cadastrar Livro")
            print("3 - Atualizar Livro")

            print("3 - Pesquisar Usuarios")
            print("4 - Cadastrar Usuario")
            print("5 - Atualizar Usuario")

            print("6 - Pesquisar Funcionarios")
            print("7 - Cadastrar Funcionarios")

            print("8 - Sair\n")
            opcao = input()

            if opcao in ('1', '2', '3', '4', '5', '6', '7', '8'):
                return opcao
            else:
                print("Opcao invalida!")


