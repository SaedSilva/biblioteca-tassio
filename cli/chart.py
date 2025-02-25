from domain.services.book_service import BookService
from utils.utils import enter_input
import matplotlib.pyplot as plt


class Chart:
    def __init__(self, book_service: BookService):
        self._book_service = book_service

    def start(self):
        while True:
            print("Escolha um grafico")
            print("1 - Percentual de livros por categoria")
            print("2 - Categorias mais alugadas")
            print("3 - Quantidade de livros alugados e não alugados")
            print("4 - Voltar")

            opcao = input()

            if opcao == "1":
                books_category = self._book_service.books_category()

                quantidade = list(map(lambda x: x.quantity, books_category))
                legenda = list(map(lambda x: x.category, books_category))

                plt.pie(quantidade, labels=legenda, autopct='%1.0f%%',)
                plt.title(
                    label="Percentual de livros por categoria",
                    fontdict={"fontsize": 16},
                    pad=20
                )
                plt.show()
            elif opcao == "2":
                books_category = self._book_service.books_categories_most_rented()
                fig, ax  = plt.subplots()
                quantidade = list(map(lambda x: x.quantity, books_category))
                legenda = list(map(lambda x: x.category, books_category))
                ax.bar(legenda, quantidade)
                ax.set_ylabel('Quantidade')
                ax.set_title('Quantidade de livros alugados por categoria')
                plt.show()

            elif opcao == "3":
                books_rented_not_rented = self._book_service.books_rented_not_rented()
                quantidade = [books_rented_not_rented.rented, books_rented_not_rented.not_rented]
                legenda = ['Alugados', 'Não alugados']
                plt.pie(quantidade, labels=legenda, autopct='%1.2f%%',)
                plt.title(
                    label="Quantidade de livros alugados e não alugados",
                    fontdict={"fontsize": 16},
                    pad=20
                )
                plt.show()

            elif opcao == "4":
                break

            enter_input()