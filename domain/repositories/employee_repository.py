from domain.entities.employee import Employee
from domain.repositories.sqlite_helper import SQLiteHelper


class EmployeeRepository:
    def __init__(self, sqlite_helper: SQLiteHelper = SQLiteHelper()):
        self.sqlite_helper = sqlite_helper
        self.create_table()

    def create_table(self):
        self.sqlite_helper.conn.execute('''
            CREATE TABLE IF NOT EXISTS employees (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')

    def insert(self, employee: Employee):
        self.sqlite_helper.conn.execute(
            'INSERT INTO employees (name, username, password) VALUES (?, ?, ?)',
            (employee.name, employee.username, employee.password)
        )
        self.sqlite_helper.conn.commit()

    def update(self, employee: Employee):
        self.sqlite_helper.conn.execute(
            'UPDATE employees SET name = ?, username = ?, password = ? WHERE id = ?',
            (employee.name, employee.username, employee.password, employee.id)
        )
        self.sqlite_helper.conn.commit()

    def delete(self, employee: Employee):
        self.sqlite_helper.conn.execute(
            'DELETE FROM employees WHERE id = ?',
            (employee.id,)
        )
        self.sqlite_helper.conn.commit()

    def find_all(self) -> list[Employee]:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM employees')
        employees: list[Employee] = []
        for row in cursor:
            employees.append(Employee(row[0], row[1], row[2], row[3]))
        return employees

    def find_by_id(self, id: int) -> Employee:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM employees WHERE id = ?', (id,))
        row = cursor.fetchone()
        return Employee(row[0], row[1], row[2], row[3]) if row else None

    def find_by_username(self, username: str) -> Employee:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM employees WHERE username = ?', (username,))
        row = cursor.fetchone()
        return Employee(row[0], row[1], row[2], row[3]) if row else None
