from validate import validate_title, validate_author, validate_year, validate_price

class Book:
    total_books = 0

    def __init__(self, title, author, year, price):
        self._title = validate_title(title)
        self._author = validate_author(author)
        self._year = validate_year(year)
        self._price = validate_price(price)
        self._status = "available"  # available, checked_out, damaged
        Book.total_books += 1

    @property
    def title(self):
        return self._title

    @property
    def author(self):
        return self._author

    @property
    def year(self):
        return self._year

    @year.setter
    def year(self, value):
        self._year = validate_year(value)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = validate_price(value)

    @property
    def status(self):
        return self._status

    # Методы изменения состояния
    def check_out(self):
        if self._status == "available":
            self._status = "checked_out"
            print(f"✓ Книга '{self.title}' выдана.")
        elif self._status == "checked_out":
            print(f"⚠ Книга '{self.title}' уже выдана, нельзя выдать повторно.")
        elif self._status == "damaged":
            print(f"✗ Книга '{self.title}' повреждена, выдача невозможна.")
        else:
            print(f"❓ Неизвестный статус книги '{self.title}'.")

    def return_book(self, damaged=False):
        if self._status == "checked_out":
            if damaged:
                self._status = "damaged"
                print(f"⚠ Книга '{self.title}' возвращена с повреждениями.")
            else:
                self._status = "available"
                print(f"✓ Книга '{self.title}' возвращена в хорошем состоянии.")
        elif self._status == "available":
            print(f"⚠ Книга '{self.title}' не была выдана, возврат невозможен.")
        elif self._status == "damaged":
            print(f"⚠ Книга '{self.title}' уже повреждена, требуется ремонт.")
        else:
            print(f"❓ Неизвестный статус книги '{self.title}'.")

    def repair(self):
        if self._status == "damaged":
            self._status = "available"
            print(f"🔧 Книга '{self.title}' отремонтирована и снова доступна.")
        else:
            print(f"ℹ Книга '{self.title}' не требует ремонта (статус: {self._status}).")

    # Магические методы
    def __str__(self):
        status_rus = {
            "available": "в наличии",
            "checked_out": "выдана",
            "damaged": "повреждена"
        }.get(self._status, self._status)
        return f"'{self._title}' {self._author} ({self._year}) — {self._price:.2f} руб. [{status_rus}]"

    def __repr__(self):
        return f"Book('{self._title}', '{self._author}', {self._year}, {self._price})"

    def __eq__(self, other):
        if not isinstance(other, Book):
            return False
        return (self._title == other._title and
                self._author == other._author and
                self._year == other._year and
                self._price == other._price)

    # Бизнес-методы
    def apply_discount(self, percent):
        if not isinstance(percent, (int, float)) or percent <= 0 or percent >= 100:
            raise ValueError("Скидка должна быть числом от 0 до 100 (не включая границы).")
        self._price -= self._price * (percent / 100)

    def is_modern(self):
        return self._year > 2000

    @classmethod
    def get_total_books(cls):
        return cls.total_books