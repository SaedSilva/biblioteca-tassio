from typing import Tuple

from domain.entities.book import Book
from domain.entities.customer import Customer
from domain.entities.employee import Employee
from domain.projections.book_customer import CustomerBookProjection
from domain.repositories.sqlite_helper import SQLiteHelper


class BookRepository:
    def __init__(self, sqlite_helper: SQLiteHelper = SQLiteHelper()):
        self._sqlite_helper = sqlite_helper
        self.create_table()

    def create_table(self):
        self._sqlite_helper.conn.execute('''
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
        self._sqlite_helper.conn.execute(
            'INSERT INTO books (title, description, author, price, category) VALUES (?, ?, ?, ?, ?)',
            (entity.title, entity.description, entity.author, entity.price, entity.category)
        )
        self._sqlite_helper.conn.commit()

    def update(self, entity: Book):
        self._sqlite_helper.conn.execute(
            'UPDATE books SET title = ?, description = ?, author = ?, price = ?, category = ? WHERE id = ?',
            (entity.title, entity.description, entity.author, entity.price, entity.category, entity.id)
        )
        self._sqlite_helper.conn.commit()

    def delete(self, entity: Book):
        self._sqlite_helper.conn.execute(
            'DELETE FROM books WHERE id = ?',
            (entity.id,)
        )
        self._sqlite_helper.conn.commit()

    def find_all(self) -> list[Book]:
        cursor = self._sqlite_helper.conn.execute('SELECT * FROM books')
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities

    def find_book_by_title(self, title: str) -> list[Book]:
        cursor = self._sqlite_helper.conn.execute('SELECT * FROM books WHERE title LIKE ?', ('%' + title + '%',))
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities

    def find_book_by_category(self, category: str) -> list[Book]:
        cursor = self._sqlite_helper.conn.execute('SELECT * FROM books WHERE category LIKE ?', ('%' + category + '%',))
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities

    def find_book_by_author(self, author: str) -> list[Book]:
        cursor = self._sqlite_helper.conn.execute('SELECT * FROM books WHERE author LIKE ?', ('%' + author + '%',))
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities

    def find_all_not_rented(self) -> list[Book]:
        cursor = self._sqlite_helper.conn.execute('SELECT * FROM books WHERE rented_by IS NULL')
        entities: list[Book] = []
        for row in cursor:
            entities.append(Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
        return entities

    def find_all_rented(self) -> list[CustomerBookProjection]:
        cursor = self._sqlite_helper.conn.execute('''
            SELECT * FROM books
            INNER JOIN main.customers c on books.rented_by = c.cpf
        ''')
        entities: list[CustomerBookProjection] = []
        for row in cursor:
            book = Book(row[0], row[1], row[2], row[3], row[4], row[5], row[6])
            customer = Customer(row[7], row[8])
            entities.append(CustomerBookProjection(book, customer))
        return entities

    def rent_book(self, book_id: int, customer_cpf: str):
        self._sqlite_helper.conn.execute(
            'UPDATE books SET rented_by = ? WHERE id = ?',
            (customer_cpf, book_id)
        )
        self._sqlite_helper.conn.commit()

    def return_book(self, book_id: int):
        self._sqlite_helper.conn.execute(
            'UPDATE books SET rented_by = NULL WHERE id = ?',
            (book_id,)
        )
        self._sqlite_helper.conn.commit()