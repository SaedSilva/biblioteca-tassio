class Book:
    def __init__(self, id: int, title: str, description: str, author: str, price: float, category: str, rented_by: str | None):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.price = price
        self.category = category
        self.rented_by = rented_by

    def __str__(self):
        rented_by = self.rented_by if self.rented_by else ''
        return f'{self.id:<5} {self.title:<50} {self.description:<60} {self.author:<30} {self.price:<10} {self.category:<30} {rented_by:<30}'

    @staticmethod
    def header():
        return f'{"ID":<5} {"Title":<50} {"Description":<60} {"Author":<30} {"Price":<10} {"Category":<30} {"Rented by":<30}'



