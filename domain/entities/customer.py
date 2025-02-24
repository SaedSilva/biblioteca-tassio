class Customer:
    def __init__(self, cpf: str, name: str):
        self.cpf = cpf
        self.name = name

    def __str__(self):
        return f'{self.cpf:<15} {self.name:<30}'

    @staticmethod
    def header():
        return f'{"CPF":<15} {"Name":<30}'
