import hashlib

from domain.entities.customer import Customer
from domain.entities.employee import Employee
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository


class CustomerService:
    def __init__(self, repository: CustomerRepository = CustomerRepository()):
        self.user_repository = repository

    def find_all(self):
        return self.user_repository.find_all()

    def insert(self, cpf: str, name: str):
        customer = Customer(cpf, name)
        self.user_repository.insert(customer)

    def update(self, old_cpf: str, cpf: str, name: str):
        customer = Customer(cpf, name)
        self.user_repository.update(old_cpf, customer)

    def delete(self, cpf: str):
        customer = Customer(cpf, None)
        self.user_repository.delete(customer)


