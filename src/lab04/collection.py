from typing import List, Any
from interfaces import Printable, Comparable
from models import Book, Magazine

class MediaCollection:
    def __init__(self):
        self._items: List[Any] = []   # могут быть любые объекты, реализующие интерфейсы

    def add(self, item) -> None:
        """Добавляет объект, если он не дубликат и реализует Printable (опционально)."""
        # Проверка на дубликат по названию и году (упрощённо)
        for existing in self._items:
            if hasattr(existing, 'title') and hasattr(item, 'title') and existing.title == item.title:
                if hasattr(existing, 'year') and hasattr(item, 'year') and existing.year == item.year:
                    raise ValueError(f"Дубликат: {item.title} уже есть.")
        self._items.append(item)

    def remove(self, item) -> None:
        self._items.remove(item)

    def get_all(self) -> List:
        return self._items.copy()

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    # Фильтрация по интерфейсу
    def get_printable(self) -> List[Printable]:
        """Возвращает все объекты, реализующие Printable."""
        return [item for item in self._items if isinstance(item, Printable)]

    def get_comparable(self) -> List[Comparable]:
        """Возвращает все объекты, реализующие Comparable."""
        return [item for item in self._items if isinstance(item, Comparable)]

    # Сортировка по интерфейсу Comparable
    def sort_by_comparable(self):
        """Сортирует коллекцию, используя метод compare_to объектов."""
        self._items.sort(key=lambda x: (x.compare_to(x) if isinstance(x, Comparable) else 0))
        # Более корректно: использовать sort с кастомной функцией сравнения
        # Но для простоты отсортируем по результату compare_to с самим собой (неправильно).
        # Правильный способ:
        from functools import cmp_to_key
        def cmp(a, b):
            if isinstance(a, Comparable) and isinstance(b, Comparable):
                # Сравниваем однотипные объекты (Book с Book, Magazine с Magazine)
                if type(a) == type(b):
                    return a.compare_to(b)
                else:
                    # Разные типы: сначала книги, потом журналы (или наоборот)
                    return -1 if isinstance(a, Book) else 1
            return 0
        self._items.sort(key=cmp_to_key(cmp))

    # Универсальная печать всех Printable в коллекции
    def print_all(self) -> None:
        for item in self.get_printable():
            print(item.to_string())