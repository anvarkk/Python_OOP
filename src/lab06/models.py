class Book:
    def __init__(self, title: str, author: str, year: int, price: float) -> None:
        self._title: str = title
        self._author: str = author
        self._year: int = year
        self._price: float = price

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

    # Методы для протоколов (оценка 5)
    def display(self) -> str:
        return f"Book: {self.title} by {self.author} ({self.year})"

    def score(self) -> float:
        # Возвращаем рейтинг: например, цену как показатель популярности
        return self.price

    def __str__(self) -> str:
        return self.display()


class Magazine:
    def __init__(self, title: str, issue: int, year: int, price: float) -> None:
        self._title: str = title
        self._issue: int = issue
        self._year: int = year
        self._price: float = price

    @property
    def title(self) -> str:
        return self._title

    @property
    def issue(self) -> int:
        return self._issue

    @property
    def year(self) -> int:
        return self._year

    @property
    def price(self) -> float:
        return self._price

    def display(self) -> str:
        return f"Magazine: {self.title} #{self.issue} ({self.year})"

    def score(self) -> float:
        # Возвращаем оценку качества: например, цену
        return self.price

    def __str__(self) -> str:
        return self.display()