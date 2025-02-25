import hashlib

from domain.entities.book import Book
from domain.entities.employee import Employee
from domain.repositories.book_repository import BookRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository


class BookService:
    def __init__(self, repository: BookRepository = BookRepository()):
        self._repository = repository

    def find_all(self):
        return self._repository.find_all()

    def insert(self, title: str, description: str, author: str, price: float, category: str):
        book = Book(None, title, description, author, price, category, None)
        self._repository.insert(book)

    def update(self, id: int, title: str, description: str, author: str, price: float, category: str):
        book = Book(id, title, description, author, price, category, None)
        self._repository.update(book)

    def delete(self, id: int):
        book = Book(id, None, None, None, None, None, None)
        self._repository.delete(book)

    def search_by_title(self, title: str):
        return self._repository.find_book_by_title(title)

    def search_by_category(self, category: str):
        return self._repository.find_book_by_category(category)

    def search_by_author(self, author: str):
        return self._repository.find_book_by_author(author)



    def find_all_not_rented(self):
        return self._repository.find_all_not_rented()

    def find_all_rented(self):
        return self._repository.find_all_rented()

    def rent_book(self, book_id: int, customer_cpf: str):
        try:
            self._repository.rent_book(book_id, customer_cpf)
            print("Livro alugado com sucesso!")
        except Exception as e:
            print(e)
            print("Erro ao alugar livro!")

    def return_book(self, book_id: int):
        self._repository.return_book(book_id)

    def books_category(self):
        return self._repository.books_category()

    def books_categories_most_rented(self):
        return self._repository.categories_most_rented()

    def books_rented_not_rented(self):
        return self._repository.books_rented_and_not_rented()

