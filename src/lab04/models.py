from interfaces import Printable, Comparable

class Book(Printable, Comparable):
    total_books = 0

    def __init__(self, title: str, author: str, year: int, price: float):
        if not title or not title.strip():
            raise ValueError("Название не может быть пустым.")
        if not author or not author.strip():
            raise ValueError("Автор не может быть пустым.")
        if not isinstance(year, int) or year < 1440 or year > 2025:
            raise ValueError("Год должен быть от 1440 до 2025.")
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        self._title = title.strip()
        self._author = author.strip()
        self._year = year
        self._price = float(price)
        Book.total_books += 1

    # Геттеры
    @property
    def title(self): return self._title
    @property
    def author(self): return self._author
    @property
    def year(self): return self._year
    @property
    def price(self): return self._price

    # Реализация Printable
    def to_string(self) -> str:
        return f"Book: {self.title} by {self.author} ({self.year}) - ${self.price:.2f}"

    # Реализация Comparable (сравнение по году)
    def compare_to(self, other) -> int:
        if not isinstance(other, Book):
            raise TypeError("Можно сравнивать только с Book")
        if self.year < other.year:
            return -1
        elif self.year > other.year:
            return 1
        else:
            return 0

    def __str__(self):
        return self.to_string()

class Magazine(Printable, Comparable):
    def __init__(self, title: str, issue_number: int, month: str, year: int, price: float):
        if not title or not title.strip():
            raise ValueError("Название не может быть пустым.")
        if issue_number <= 0:
            raise ValueError("Номер выпуска должен быть положительным.")
        if not month or not month.strip():
            raise ValueError("Месяц не может быть пустым.")
        if not isinstance(year, int) or year < 1900 or year > 2025:
            raise ValueError("Год вне диапазона.")
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        self._title = title.strip()
        self._issue_number = issue_number
        self._month = month.strip()
        self._year = year
        self._price = float(price)

    @property
    def title(self): return self._title
    @property
    def issue_number(self): return self._issue_number
    @property
    def month(self): return self._month
    @property
    def year(self): return self._year
    @property
    def price(self): return self._price

    # Реализация Printable
    def to_string(self) -> str:
        return f"Magazine: {self.title} #{self.issue_number} ({self.month} {self.year}) - ${self.price:.2f}"

    # Реализация Comparable (сравнение по цене)
    def compare_to(self, other) -> int:
        if not isinstance(other, Magazine):
            raise TypeError("Можно сравнивать только с Magazine")
        if self.price < other.price:
            return -1
        elif self.price > other.price:
            return 1
        else:
            return 0

    def __str__(self):
        return self.to_string()