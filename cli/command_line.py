from cli.auth import Auth
from cli.chart import Chart
from cli.customer import CustomerCli
from cli.employee import EmployeeCli
from cli.library import Library
from domain.entities.book import Book
from domain.repositories.book_repository import BookRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository
from domain.repositories.sqlite_helper import SQLiteHelper
from domain.services.auth_service import AuthService
from domain.services.book_service import BookService
from domain.services.customer_service import CustomerService
from domain.services.employee_service import EmployeeService


class CommandLine:
    def start(self):
        sqlite_helper = SQLiteHelper()
        employee_repository = EmployeeRepository(sqlite_helper)
        auth_service = AuthService(employee_repository)
        auth_cli = Auth(auth_service)

        if auth_cli.start():
            customer_repository = CustomerRepository(sqlite_helper)
            customer_service = CustomerService(customer_repository)

            book_repository = BookRepository(sqlite_helper)
            book_service = BookService(book_repository)
            employee_service = EmployeeService(employee_repository)

            library_cli = Library(book_service)
            customer_cli = CustomerCli(customer_service)
            employee_cli = EmployeeCli(employee_service, auth_service)
            chart_cli = Chart(book_service)

            print("Bem vindo ao Tassio Libraries\n")
            while True:
                opcao: str = self.input_opcao()
                if opcao == "1":
                    library_cli.start()
                elif opcao == "2":
                    customer_cli.start()
                elif opcao == "3":
                    employee_cli.start()
                elif opcao == "4":
                    chart_cli.start()

                elif opcao == "5":
                    break


        print("Programa finalizado!")

    def input_opcao(self) -> str:
        while True:
            print("Escolha uma opçao")
            print("1 - Livros")
            print("2 - Clientes")
            print("3 - Funcionarios")
            print("4 - Graficos")

            print("5 - Sair\n")
            opcao = input()

            if opcao in ('1', '2', '3', '4', '5'):
                return opcao
            else:
                print("Opcao invalida!")


