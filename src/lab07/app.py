from typing import List, Callable, Optional
from models import Book
from exceptions import DuplicateItemError, ItemNotFoundError

class BookApp:
    """Управление коллекцией книг."""

    def __init__(self) -> None:
        self._items: List[Book] = []

    def load_books(self, books: List[Book]) -> None:
        """Загружает начальный список книг (например, из файла)."""
        self._items = books.copy()

    def get_all(self) -> List[Book]:
        """Возвращает копию списка всех книг."""
        return self._items.copy()

    def add(self, book: Book) -> None:
        """
        Добавляет книгу, если нет дубликата.

        Args:
            book: Книга для добавления.

        Raises:
            DuplicateItemError: Если книга уже есть в коллекции.
        """
        if book in self._items:
            raise DuplicateItemError(f"Книга '{book.title}' уже существует.")
        self._items.append(book)

    def remove(self, title: str) -> None:
        """
        Удаляет книгу по названию.

        Args:
            title: Название книги.

        Raises:
            ItemNotFoundError: Если книга не найдена.
        """
        for i, book in enumerate(self._items):
            if book.title.lower() == title.lower():
                del self._items[i]
                return
        raise ItemNotFoundError(f"Книга '{title}' не найдена.")

    def find(self, title: str) -> Optional[Book]:
        """
        Ищет книгу по названию.

        Args:
            title: Название книги.

        Returns:
            Книгу или None, если не найдена.
        """
        for book in self._items:
            if book.title.lower() == title.lower():
                return book
        return None

    def filter(self, predicate: Callable[[Book], bool]) -> List[Book]:
        """
        Возвращает список книг, удовлетворяющих условию.

        Args:
            predicate: Функция-фильтр.

        Returns:
            Отфильтрованный список.
        """
        return [book for book in self._items if predicate(book)]

    def sort(self, key_func: Callable[[Book], any], reverse: bool = False) -> List[Book]:
        """
        Возвращает новый отсортированный список книг.

        Args:
            key_func: Функция, извлекающая ключ сортировки.
            reverse: Обратный порядок.

        Returns:
            Отсортированный список.
        """
        return sorted(self._items, key=key_func, reverse=reverse)

    def __len__(self) -> int:
        return len(self._items)