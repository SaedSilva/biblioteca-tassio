from domain.entities.book import Book
from domain.entities.customer import Customer


class CustomerBookProjection:
    def __init__(self, book: Book, customer: Customer):
        self.book = book
        self.customer = customer

    def __str__(self):
        return f'{self.book.id:<5} {self.book.title:<50} {self.book.description:<60} {self.book.author:<30} {self.book.price:<10} {self.book.category:<30} {self.customer.cpf:<15} {self.customer.name:<30}'

    @staticmethod
    def header():
        return f'{"ID":<5} {"Title":<50} {"Description":<60} {"Author":<30} {"Price":<10} {"Category":<30} {"Rented by":<30} {"CPF":<15} {"Customer name":<30}'
