class Book:
    def __init__(self, title: str, author: str, year: int, price: float):
        self._title = title
        self._author = author
        self._year = year
        self._price = price

    @property
    def title(self): return self._title
    @property
    def author(self): return self._author
    @property
    def year(self): return self._year
    @property
    def price(self): return self._price

    def __str__(self):
        return f"Book: {self.title} by {self.author} ({self.year}) - ${self.price:.2f}"

    def __repr__(self):
        return str(self)

class Magazine:
    def __init__(self, title: str, issue: int, year: int, price: float):
        self._title = title
        self._issue = issue
        self._year = year
        self._price = price

    @property
    def title(self): return self._title
    @property
    def issue(self): return self._issue
    @property
    def year(self): return self._year
    @property
    def price(self): return self._price

    def __str__(self):
        return f"Magazine: {self.title} #{self.issue} ({self.year}) - ${self.price:.2f}"

    def __repr__(self):
        return str(self)