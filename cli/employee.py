from domain.entities.employee import Employee
from domain.services.auth_service import AuthService
from domain.services.employee_service import EmployeeService
from utils.utils import enter_input


class EmployeeCli:
    def __init__(self, employee_service: EmployeeService, auth_service: AuthService):
        self.employee_service = employee_service
        self.auth_service = auth_service

    def start(self):
        while True:
            opcao = self.input_opcao()

            if opcao == "1":
                name = input("Digite o nome do funcionario: ")
                username = input("Digite o username do funcionario: ")
                password = input("Digite a senha do funcionario: ")
                self.auth_service.signup(name, username, password)
                print("Funcionario cadastrado com sucesso!\n")
                enter_input()

            elif opcao == "2":
                id = int(input("Digite o id do funcionario: "))
                name = input("Digite o nome do funcionario: ")
                username = input("Digite o username do funcionario: ")
                password = input("Digite a senha do funcionario: ")
                self.auth_service.update(id, name, username, password)
                print("Funcionario atualizado com sucesso!\n")
                enter_input()

            elif opcao == "3":
                id = int(input("Digite o id do funcionario: "))
                self.employee_service.delete(id)
                print("Funcionario deletado com sucesso!\n")
                enter_input()

            elif opcao == "4":
                funcionarios = self.employee_service.find_all()
                if len(funcionarios) == 0:
                    print("Nenhum funcionario encontrado!\n")
                    enter_input()
                else:
                    print("Funcionarios encontrados:")
                    print(Employee.header())
                    for funcionario in funcionarios:
                        print(funcionario)
                    enter_input()

            elif opcao == "5":
                break

    def input_opcao(self) -> str:
        while True:
            print("\nEscolha uma opçao")
            print("1 - Adicionar funcionario")
            print("2 - Atualizar funcionario")
            print("3 - Remover funcionario")
            print("4 - Listar funcionarios")
            print("5 - Sair\n")
            opcao = input()
            if opcao in ('1', '2', '3', '4', '5'):
                return opcao
            else:
                print("Opcao invalida!")
