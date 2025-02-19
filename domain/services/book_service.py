import hashlib

from domain.entities.employee import Employee
from domain.repositories.book_repository import BookRepository
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository


class BookService:
    def __init__(self, repository: BookRepository = BookRepository()):
        self._repository = repository
