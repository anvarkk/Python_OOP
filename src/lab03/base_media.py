from abc import ABC, abstractmethod

class Media(ABC):
    """Абстрактный базовый класс для всех медиа-объектов."""
    
    def __init__(self, title: str, year: int, price: float):
        self._title = title
        self._year = year
        self._price = price
    
    @property
    def title(self) -> str:
        return self._title
    
    @property
    def year(self) -> int:
        return self._year
    
    @property
    def price(self) -> float:
        return self._price
    
    @price.setter
    def price(self, value: float):
        if value <= 0:
            raise ValueError("Цена должна быть положительной.")
        self._price = value
    
    @abstractmethod
    def get_info(self) -> str:
        """Возвращает информацию об объекте. Должен быть переопределён."""
        pass
    
    def __eq__(self, other):
        if not isinstance(other, Media):
            return False
        return (self.title == other.title and
                self.year == other.year and
                self.price == other.price)
    
    def __str__(self):
        return self.get_info()