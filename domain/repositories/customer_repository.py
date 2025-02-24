from domain.entities.customer import Customer
from domain.entities.employee import Employee
from domain.repositories.sqlite_helper import SQLiteHelper


class CustomerRepository:
    def __init__(self, sqlite_helper: SQLiteHelper = SQLiteHelper()):
        self.sqlite_helper = sqlite_helper
        self.create_table()

    def create_table(self):
        self.sqlite_helper.conn.execute('''
            CREATE TABLE IF NOT EXISTS customers (
                cpf TEXT PRIMARY KEY,
                name TEXT NOT NULL
            );
        ''')

    def insert(self, entity: Customer):
        self.sqlite_helper.conn.execute(
            'INSERT INTO customers (cpf, name) VALUES (?, ?)',
            (entity.cpf, entity.name)
        )
        self.sqlite_helper.conn.commit()

    def update(self, cpf: str, entity: Customer):
        self.sqlite_helper.conn.execute(
            'UPDATE customers SET cpf = ?, name = ? WHERE cpf = ?',
            (entity.cpf, entity.name, cpf)
        )
        self.sqlite_helper.conn.commit()

    def delete(self, entity: Customer):
        self.sqlite_helper.conn.execute(
            'DELETE FROM customers WHERE cpf = ?',
            (entity.cpf,)
        )
        self.sqlite_helper.conn.commit()

    def find_all(self) -> list[Customer]:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM customers')
        entities: list[Customer] = []
        for row in cursor:
            entities.append(Customer(row[0], row[1]))
        return entities
