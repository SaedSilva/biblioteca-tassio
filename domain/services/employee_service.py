from domain.entities.employee import Employee
from domain.repositories.employee_repository import EmployeeRepository


class EmployeeService:
    def __init__(self, employee_repository: EmployeeRepository):
        self.employee_repository = employee_repository

    def find_all(self):
        return self.employee_repository.find_all()

    def insert(self, name: str, username: str, password: str):
        employee = Employee(None, name, username, password)
        self.employee_repository.insert(employee)

    def update(self, id: int, name: str, username: str, password: str):
        employee = Employee(id, name, username, password)
        self.employee_repository.update(employee)

    def delete(self, id: int):
        employee = Employee(id, None, None, None)
        self.employee_repository.delete(employee)

