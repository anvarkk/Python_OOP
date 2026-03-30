from base_media import Media

class Magazine(Media):
    def __init__(self, title: str, issue_number: int, month: str, year: int, price: float):
        if issue_number <= 0:
            raise ValueError("Номер выпуска должен быть положительным.")
        if not month or not month.strip():
            raise ValueError("Название месяца не может быть пустым.")
        if year < 1900 or year > 2025:
            raise ValueError("Год вне допустимого диапазона.")
        if price <= 0:
            raise ValueError("Цена должна быть положительной.")
        
        super().__init__(title, year, price)
        self._issue_number = issue_number
        self._month = month.strip()
    
    @property
    def issue_number(self) -> int:
        return self._issue_number
    
    @property
    def month(self) -> str:
        return self._month
    
    def get_info(self) -> str:
        """Переопределённый метод базового класса."""
        return (f"Журнал: '{self.title}' | Выпуск №{self.issue_number} "
                f"({self.month} {self.year}) | Цена: {self.price:.2f} руб.")
    
    def apply_seasonal_discount(self, discount_percent: float):
        """Специфический метод журнала."""
        if discount_percent <= 0 or discount_percent >= 100:
            raise ValueError("Некорректная скидка.")
        self.price -= self.price * (discount_percent / 100)