class Book:
    """Книга с названием, автором, годом и ценой."""
    def __init__(self, title: str, author: str, year: int, price: float) -> None:
        self._title = title
        self._author = author
        self._year = year
        self._price = price

    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @property
    def price(self) -> float:
        return self._price

    def to_dict(self) -> dict:
        """Преобразует книгу в словарь для JSON."""
        return {
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "price": self.price
        }

    @classmethod
    def from_dict(cls, data: dict) -> 'Book':
        """Создаёт книгу из словаря."""
        return cls(data["title"], data["author"], data["year"], data["price"])

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Book):
            return False
        return (self.title == other.title and
                self.author == other.author and
                self.year == other.year and
                self.price == other.price)

    def __str__(self) -> str:
        return f"'{self.title}' by {self.author} ({self.year}) — {self.price:.2f} руб. "

    def __repr__(self) -> str:
        return f"Book(title='{self.title}', author='{self.author}', year={self.year}, price={self.price})"