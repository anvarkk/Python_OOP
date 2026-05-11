from typing import TypeVar, Generic, Callable, Optional, List

# ----- Протоколы (для оценки 5) -----
from typing import Protocol

class Displayable(Protocol):
    def display(self) -> str:
        ...

class Scorable(Protocol):
    def score(self) -> float:
        ...

# ----- TypeVar для оценки 3-4 -----
T = TypeVar('T')          # для простой generic-коллекции
R = TypeVar('R')          # для map с преобразованием типа

# ----- TypeVar с ограничениями для оценки 5 -----
D = TypeVar('D', bound=Displayable)
S = TypeVar('S', bound=Scorable)

# ----- Generic-коллекция -----
class TypedCollection(Generic[T]):
    """Generic-версия коллекции из ЛР-2 с поддержкой find, filter, map."""
    def __init__(self) -> None:
        self._items: List[T] = []

    def add(self, item: T) -> None:
        """Добавляет элемент в коллекцию."""
        self._items.append(item)

    def remove(self, item: T) -> None:
        """Удаляет элемент из коллекции."""
        self._items.remove(item)

    def get_all(self) -> List[T]:
        """Возвращает копию списка всех элементов."""
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    # ----- Новые методы для оценки 4 -----
    def find(self, predicate: Callable[[T], bool]) -> Optional[T]:
        """Возвращает первый элемент, удовлетворяющий предикату, или None."""
        for item in self._items:
            if predicate(item):
                return item
        return None

    def filter(self, predicate: Callable[[T], bool]) -> List[T]:
        """Возвращает список всех элементов, удовлетворяющих предикату."""
        return [item for item in self._items if predicate(item)]

    def map(self, transform: Callable[[T], R]) -> List[R]:
        """Применяет функцию преобразования к каждому элементу и возвращает список результатов."""
        return [transform(item) for item in self._items]

    # ----- Дополнительно: метод для демонстрации работы с протоколами -----
    def display_all(self) -> None:
        for item in self._items:
            # предполагается, что T поддерживает display() – для коллекций с bound=Displayable
            if hasattr(item, 'display'):
                print(item.display())