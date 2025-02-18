import hashlib

from domain.entities.employee import Employee
from domain.repositories.employee_repository import EmployeeRepository


class AuthService:
    def __init__(self, user_repository: EmployeeRepository = EmployeeRepository()):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username.lower())
        return user and user.password == self._hash_password(password)

    def signup(self, name: str, username: str, password: str) -> bool:
        if len(name) < 3:
            return False
        if len(username) < 3:
            return False
        if len(password) < 3:
            return False
        if self.user_repository.find_by_username(username):
            return False
        self.user_repository.insert(Employee(None, name, username.lower(), self._hash_password(password)))
        return True

    def _hash_password(self, password: str) -> str:
        hash_object = hashlib.sha256()
        hash_object.update(password.encode())
        hash_password = hash_object.hexdigest()
        return hash_password
