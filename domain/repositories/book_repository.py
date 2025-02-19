from domain.entities.book import Book
from domain.entities.customer import Customer
from domain.entities.employee import Employee
from domain.repositories.sqlite_helper import SQLiteHelper


class BookRepository:
    def __init__(self, sqlite_helper: SQLiteHelper = SQLiteHelper()):
        self.sqlite_helper = sqlite_helper
        self.create_table()

    def create_table(self):
        self.sqlite_helper.conn.execute('''
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                author TEXT NOT NULL,
                price REAL NOT NULL,
                category TEXT NOT NULL,
                rented_by TEXT,
                FOREIGN KEY (rented_by) REFERENCES customers(cpf)
            );
        ''')

    def insert(self, entity: Book):
        self.sqlite_helper.conn.execute(
            'INSERT INTO books (title, description, author, price, category) VALUES (?, ?, ?, ?, ?)',
            (entity.title, entity.description, entity.author, entity.price, entity.category)
        )
        self.sqlite_helper.conn.commit()

    def update(self, entity: Book):
        self.sqlite_helper.conn.execute(
            'UPDATE books SET title = ?, description = ?, author = ?, price = ?, category = ? WHERE id = ?',
            (entity.title, entity.description, entity.author, entity.price, entity.category, entity.id)
        )
        self.sqlite_helper.conn.commit()

    def delete(self, entity: Book):
        self.sqlite_helper.conn.execute(
            'DELETE FROM books WHERE id = ?',
            (entity.id,)
        )
        self.sqlite_helper.conn.commit()

    def find_all(self) -> list[Book]:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM books')
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities
