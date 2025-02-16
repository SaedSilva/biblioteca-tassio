from domain.entities.user import User
from domain.repositories.user_repository import UserRepository


class AuthService:
    def __init__(self, user_repository: UserRepository = UserRepository()):
        self.user_repository = user_repository

    def authenticate(self, username: str, password: str) -> bool:
        user = self.user_repository.find_by_username(username.lower())
        return user and user.password == password

    def signup(self, name: str, username: str, password: str) -> bool:
        if len(name) < 3:
            return False
        if len(username) < 3:
            return False
        if len(password) < 3:
            return False
        if self.user_repository.find_by_username(username):
            return False
        self.user_repository.insert(User(None, name, username.lower(), password))
        return True
