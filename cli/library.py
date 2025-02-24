from typing import List

from domain.entities.book import Book
from domain.projections.book_customer import CustomerBookProjection
from domain.services.book_service import BookService
from utils.utils import enter_input


class Library:
    def __init__(self, service: BookService):
        self._service = service
        print()

    def start(self):
        while True:
            opcao = self.input_opcao()

            if opcao == "1":
                titulo = input("Digite o titulo do livro: ")
                livros = self._service.search_by_title(titulo)
                if len(livros) == 0:
                    print("Nenhum livro encontrado com esse titulo!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(Book.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "2":
                categoria = input("Digite a categoria do livro: ")
                livros = self._service.search_by_category(categoria)
                if len(livros) == 0:
                    print("Nenhum livro encontrado com essa categoria!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(Book.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "3":
                autor = input("Digite o autor do livro: ")
                livros = self._service.search_by_author(autor)
                if len(livros) == 0:
                    print("Nenhum livro encontrado com esse autor!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(Book.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "4":
                livros = self._service.find_all()
                if len(livros) == 0:
                    print("Nenhum livro encontrado!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(Book.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "5":
                livros = self._service.find_all_not_rented()
                if len(livros) == 0:
                    print("Nenhum livro nao alugado encontrado!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(Book.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "6":
                livros: List[CustomerBookProjection] = self._service.find_all_rented()
                if len(livros) == 0:
                    print("Nenhum livro alugado encontrado!\n")
                    enter_input()
                else:
                    print("Livros encontrados:")
                    print(CustomerBookProjection.header())
                    for livro in livros:
                        print(livro)
                    enter_input()

            elif opcao == "7":
                id = int(input("Digite o id do livro: "))
                cpf = input("Digite o cpf do cliente: ")
                self._service.rent_book(id, cpf)
                print("Livro alugado com sucesso!\n")
                enter_input()

            elif opcao == "8":
                id = int(input("Digite o id do livro: "))
                self._service.return_book(id)
                print("Livro devolvido com sucesso!\n")
                enter_input()

            elif opcao == "9":
                titulo = input("Digite o titulo do livro: ")
                descricao = input("Digite a descricao do livro: ")
                autor = input("Digite o autor do livro: ")
                preco = float(input("Digite o preco do livro: "))
                categoria = input("Digite a categoria do livro: ")
                self._service.insert(titulo, descricao, autor, preco, categoria)
                print("Livro adicionado com sucesso!\n")
                enter_input()

            elif opcao == "10":
                id = int(input("Digite o id do livro: "))
                titulo = input("Digite o titulo do livro: ")
                descricao = input("Digite a descricao do livro: ")
                autor = input("Digite o autor do livro: ")
                preco = float(input("Digite o preco do livro: "))
                categoria = input("Digite a categoria do livro: ")
                self._service.update(id, titulo, descricao, autor, preco, categoria)
                print("Livro atualizado com sucesso!\n")
                enter_input()

            elif opcao == "11":
                id = int(input("Digite o id do livro: "))
                self._service.delete(id)
                print("Livro removido com sucesso!\n")
                enter_input()

            elif opcao == "12":
                break

    def input_opcao(self) -> str:
        while True:
            print("1 - Pesquisar livro por titulo")
            print("2 - Pesquisar livro por categoria")
            print("3 - Pesquisar livro por autor")
            print("4 - Listar todos os livros")
            print("5 - Listar todos os nao alugados")
            print("6 - Listar todos os livros alugados")
            print("7 - Alugar um livro")
            print("8 - Devolver um livro")
            print("9 - Adicionar um livro")
            print("10 - Atualizar um livro")
            print("11 - Remover um livro")
            print("12 - Sair")

            opcao = input()
            if opcao in ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]:
                return opcao
            print("Opcao invalida, tente novamente")
