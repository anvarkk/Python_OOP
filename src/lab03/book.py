from base_media import Media

class Book(Media):
    total_books = 0
    
    def __init__(self, title: str, author: str, year: int, price: float):
        # Валидация
        if not author or not author.strip():
            raise ValueError("Имя автора не может быть пустым.")
        if not isinstance(year, int) or year < 1440 or year > 2025:
            raise ValueError("Год издания должен быть целым числом от 1440 до 2025.")
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        
        super().__init__(title, year, price)
        self._author = author.strip()
        Book.total_books += 1
    
    @property
    def author(self) -> str:
        return self._author
    
    def get_info(self) -> str:
        """Переопределённый метод базового класса."""
        return f"Книга: '{self.title}' | Автор: {self.author} | {self.year} г. | Цена: {self.price:.2f} руб."
    
    def apply_discount(self, percent: float):
        """Бизнес-метод книги."""
        if percent <= 0 or percent >= 100:
            raise ValueError("Скидка должна быть от 0 до 100 (исключая границы).")
        self.price -= self.price * (percent / 100)
    
    def is_modern(self) -> bool:
        return self.year > 2000
    
    @classmethod
    def get_total_books(cls):
        return cls.total_books