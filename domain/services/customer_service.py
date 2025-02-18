import hashlib

from domain.entities.employee import Employee
from domain.repositories.customer_repository import CustomerRepository
from domain.repositories.employee_repository import EmployeeRepository


class CustomerService:
    def __init__(self, repository: CustomerRepository = CustomerRepository()):
        self.user_repository = repository


