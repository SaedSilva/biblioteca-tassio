from domain.entities.user import User
from domain.repositories.sqlite_helper import SQLiteHelper


class UserRepository:
    def __init__(self, sqlite_helper: SQLiteHelper):
        self.sqlite_helper = sqlite_helper
        self.create_table()

    def create_table(self):
        self.sqlite_helper.conn.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                username TEXT NOT NULL,
                password TEXT NOT NULL
            );
        ''')

    def insert(self, user: User):
        self.sqlite_helper.conn.execute(
            'INSERT INTO users (name, username, password) VALUES (?, ?, ?)',
            (user.name, user.username, user.password)
        )
        self.sqlite_helper.conn.commit()

    def update(self, user: User):
        self.sqlite_helper.conn.execute(
            'UPDATE users SET name = ?, username = ?, password = ? WHERE id = ?',
            (user.name, user.username, user.password, user.id)
        )
        self.sqlite_helper.conn.commit()

    def delete(self, user: User):
        self.sqlite_helper.conn.execute(
            'DELETE FROM users WHERE id = ?',
            (user.id,)
        )
        self.sqlite_helper.conn.commit()

    def find_all(self) -> list[User]:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM users')
        users: list[User] = []
        for row in cursor:
            users.append(User(row[0], row[1], row[2], row[3]))
        return users

    def find_by_id(self, id: int) -> User:
        cursor = self.sqlite_helper.conn.execute('SELECT * FROM users WHERE id = ?', (id,))
        row = cursor.fetchone()
        return User(row[0], row[1], row[2], row[3]) if row else None
