from domain.entities.customer import Customer
from domain.entities.employee import Employee
from domain.repositories.sqlite_helper import SQLiteHelper


class EmployeeRepository:
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

    def insert(self, entity: Employee):
        self.sqlite_helper.conn.execute(
            'INSERT INTO customers (cpf, name) VALUES (?, ?)',
            (entity.name, entity.username, entity.password)
        )
        self.sqlite_helper.conn.commit()

    def update(self, entity: Customer):
        self.sqlite_helper.conn.execute(
            'UPDATE employees SET cpf = ?, name = ?',
            (entity.cpf, entity.name)
        )
        self.sqlite_helper.conn.commit()

    def delete(self, entity: Customer):
        self.sqlite_helper.conn.execute(
            'DELETE FROM employees WHERE cpf = ?',
            (entity.cpf,)
        )
        self.sqlite_helper.conn.commit()

    def find_all(self) -> list[Customer]:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM customers')
        entities: list[Customer] = []
        for row in cursor:
            entities.append(Customer(row[0], row[1]))
        return entities

    def find_by_id(self, id: int) -> Customer:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM employees WHERE id = ?', (id,))
        row = cursor.fetchone()
        return Customer(row[0], row[1]) if row else None

    def find_by_username(self, username: str) -> Customer:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM employees WHERE username = ?', (username,))
        row = cursor.fetchone()
        return Customer(row[0], row[1]) if row else None
