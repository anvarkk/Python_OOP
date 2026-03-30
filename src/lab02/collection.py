from typing import List, Optional
from model import Book

class Library:
    def __init__(self):
        self._items: List[Book] = []   # внутренний список книг

    def add(self, book: Book) -> None:
        """Добавляет книгу в библиотеку, если она не дубликат."""
        if not isinstance(book, Book):
            raise TypeError("Можно добавлять только объекты класса Book.")
        if self._is_duplicate(book):
            raise ValueError("Книга уже существует в библиотеке.")
        self._items.append(book)

    def remove(self, book: Book) -> None:
        """Удаляет книгу из библиотеки."""
        if book not in self._items:
            raise ValueError("Книга не найдена в библиотеке.")
        self._items.remove(book)

    def get_all(self) -> List[Book]:
        """Возвращает список всех книг."""
        return self._items.copy()   # возвращаем копию для защиты инкапсуляции

    def _is_duplicate(self, book: Book) -> bool:
        """Проверяет, есть ли уже такая книга в коллекции (по всем полям)."""
        for existing in self._items:
            if existing == book:
                return True
        return False

    # ----- Методы для оценки "4" -----

    def find_by_title(self, title: str) -> List[Book]:
        """Возвращает список книг с заданным названием."""
        title_lower = title.strip().lower()
        return [b for b in self._items if b.title.lower() == title_lower]

    def find_by_author(self, author: str) -> List[Book]:
        """Возвращает список книг заданного автора."""
        author_lower = author.strip().lower()
        return [b for b in self._items if b.author.lower() == author_lower]

    def find_by_year(self, year: int) -> List[Book]:
        """Возвращает список книг, изданных в указанном году."""
        return [b for b in self._items if b.year == year]

    def __len__(self) -> int:
        """Возвращает количество книг в библиотеке."""
        return len(self._items)

    def __iter__(self):
        """Позволяет итерироваться по библиотеке."""
        return iter(self._items)