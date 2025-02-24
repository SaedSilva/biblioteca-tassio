class Employee:
    def __init__(self, id: int, name: str, username: str, password: str):
        self.id = id
        self.name = name
        self.username = username
        self.password = password

    def __str__(self):
        return f'{self.id:<5} {self.name:<30} {self.username:<30}'

    @staticmethod
    def header():
        return f'{"ID":<5} {"Name":<30} {"Username":<30}'