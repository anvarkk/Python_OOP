from typing import List
from base_media import Media
from book import Book
from magazine import Magazine

class MediaCollection:
    def __init__(self):
        self._items: List[Media] = []

    def add(self, media: Media) -> None:
        if not isinstance(media, Media):
            raise TypeError("Можно добавлять только объекты, наследующие Media.")
        if self._is_duplicate(media):
            raise ValueError("Такой объект уже есть в коллекции.")
        self._items.append(media)

    def remove(self, media: Media) -> None:
        if media not in self._items:
            raise ValueError("Объект не найден в коллекции.")
        self._items.remove(media)

    def get_all(self) -> List[Media]:
        return self._items.copy()

    def _is_duplicate(self, media: Media) -> bool:
        for existing in self._items:
            if existing == media:
                return True
        return False

    def find_by_title(self, title: str) -> List[Media]:
        title_lower = title.strip().lower()
        return [m for m in self._items if m.title.lower() == title_lower]

    # Методы фильтрации по типу (для задания "5")
    def get_books(self) -> List[Book]:
        """Возвращает только книги."""
        return [item for item in self._items if isinstance(item, Book)]

    def get_magazines(self) -> List[Magazine]:
        """Возвращает только журналы."""
        return [item for item in self._items if isinstance(item, Magazine)]

    def __len__(self) -> int:
        return len(self._items)

    def __iter__(self):
        return iter(self._items)