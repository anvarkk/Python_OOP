from typing import List, Optional
from base_media import Media

class MediaCollection:
    def __init__(self):
        self._items: List[Media] = []
    
    def add(self, media: Media) -> None:
        """Добавляет объект Media в коллекцию, если он не дубликат."""
        if not isinstance(media, Media):
            raise TypeError("Можно добавлять только объекты, наследующие Media.")
        if self._is_duplicate(media):
            raise ValueError("Такой объект уже есть в коллекции.")
        self._items.append(media)
    
    def remove(self, media: Media) -> None:
        """Удаляет объект из коллекции."""
        if media not in self._items:
            raise ValueError("Объект не найден в коллекции.")
        self._items.remove(media)
    
    def get_all(self) -> List[Media]:
        """Возвращает копию списка всех объектов."""
        return self._items.copy()
    
    def _is_duplicate(self, media: Media) -> bool:
        """Проверка на дубликат (сравниваем по названию и году, можно расширить)."""
        for existing in self._items:
            if existing == media:
                return True
        return False
    
    def find_by_title(self, title: str) -> List[Media]:
        """Поиск по названию (регистронезависимый)."""
        title_lower = title.strip().lower()
        return [m for m in self._items if m.title.lower() == title_lower]
    
    def __len__(self) -> int:
        return len(self._items)
    
    def __iter__(self):
        return iter(self._items)