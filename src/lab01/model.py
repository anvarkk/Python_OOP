class Book:
    # Атрибут класса: общее количество созданных книг
    total_books = 0

    def __init__(self, title: str, author: str, year: int, price: float):
        # Проверки входных данных
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Название книги должно быть непустой строкой.")
        if not isinstance(author, str) or not author.strip():
            raise ValueError("Имя автора должно быть непустой строкой.")
        if not isinstance(year, int) or year < 1440 or year > 2025:
            raise ValueError("Год издания должен быть целым числом от 1440 до 2025.")
        if not isinstance(price, (int, float)) or price <= 0:
            raise ValueError("Цена должна быть положительным числом.")

        self._title = title.strip()
        self._author = author.strip()
        self._year = year
        self._price = float(price)

        # Увеличиваем счетчик книг
        Book.total_books += 1

    # Геттеры и сеттеры (свойства)
    @property
    def title(self) -> str:
        return self._title

    @property
    def author(self) -> str:
        return self._author

    @property
    def year(self) -> int:
        return self._year

    @year.setter
    def year(self, value: int):
        if not isinstance(value, int) or value < 1440 or value > 2025:
            raise ValueError("Год издания должен быть целым числом от 1440 до 2025.")
        self._year = value

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, value: float):
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError("Цена должна быть положительным числом.")
        self._price = float(value)

    # Магические методы
    def __str__(self) -> str:
        return f"'{self._title}' by {self._author} ({self._year}) — ${self._price:.2f}"

    def __repr__(self) -> str:
        return f"Book(title='{self._title}', author='{self._author}', year={self._year}, price={self._price:.2f})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Book):
            return False
        return (self._title == other._title and
                self._author == other._author and
                self._year == other._year and
                self._price == other._price)

    # Бизнес-методы
    def apply_discount(self, percent: float) -> None:
        """
        Применяет скидку к цене книги.
        :param percent: процент скидки (0 < percent < 100)
        """
        if not isinstance(percent, (int, float)) or percent <= 0 or percent >= 100:
            raise ValueError("Скидка должна быть числом от 0 до 100 (не включая границы).")
        self._price -= self._price * (percent / 100)

    def is_modern(self) -> bool:
        """Возвращает True, если книга издана после 2000 года."""
        return self._year > 2000

    @classmethod
    def get_total_books(cls) -> int:
        return cls.total_books