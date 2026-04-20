from abc import ABC, abstractmethod

class Printable(ABC):
    """Интерфейс для объектов, которые можно вывести в строку."""
    @abstractmethod
    def to_string(self) -> str:
        """Возвращает строковое представление объекта."""
        pass

class Comparable(ABC):
    """Интерфейс для сравнения объектов (по году или цене)."""
    @abstractmethod
    def compare_to(self, other) -> int:
        """
        Сравнивает текущий объект с other.
        Возвращает:
        -1 если self < other
         0 если self == other
         1 если self > other
        """
        pass