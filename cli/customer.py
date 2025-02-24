from domain.entities.customer import Customer
from domain.services.customer_service import CustomerService
from utils.utils import enter_input


class CustomerCli:
    def __init__(self, customer_service: CustomerService):
        self.customer_service = customer_service

    def start(self):
        while True:
            opcao = self.input_opcao()

            if opcao == "1":
                cpf = input("Digite o CPF do cliente: ")
                nome = input("Digite o nome do cliente: ")
                self.customer_service.insert(cpf, nome)
                print("Cliente cadastrado com sucesso!")

            elif opcao == "2":
                cpf = input("Digite o CPF do cliente: ")
                self.customer_service.delete(cpf)
                print("Cliente removido com sucesso!")

            elif opcao == "3":
                old_cpf = input("Digite o CPF antigo do cliente: ")
                cpf = input("Digite o CPF novo do cliente: ")
                nome = input("Digite o nome do cliente: ")
                self.customer_service.update(old_cpf, cpf, nome)
                print("Cliente atualizado com sucesso!")

            elif opcao == "4":
                clientes = self.customer_service.find_all()
                if len(clientes) == 0:
                    print("Nenhum cliente encontrado!\n")
                else:
                    print("Clientes encontrados:")
                    print(Customer.header())
                    for cliente in clientes:
                        print(cliente)

            elif opcao == "5":
                break

        enter_input()

    def input_opcao(self) -> str:
        while True:
            print("\nEscolha uma opçao")
            print("1 - Adicionar cliente")
            print("2 - Remover cliente")
            print("3 - Atualizar cliente")
            print("4 - Listar clientes")
            print("5 - Sair\n")
            opcao = input()
            if opcao in ('1', '2', '3', '4', '5'):
                return opcao
            else:
                print("Opcao invalida!")