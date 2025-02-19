class Book:
    def __init__(self, id: int, title: str, description: str, author: str, price: float, category: str, rented_by: str | None):
        self.id = id
        self.title = title
        self.description = description
        self.author = author
        self.price = price
        self.category = category
        self.rented_by = rented_by



