from typing import List, Callable, Any

class AdvancedCollection:
    def __init__(self, items=None):
        self._items = list(items) if items else []

    def add(self, item):
        self._items.append(item)

    def __len__(self):
        return len(self._items)

    def __iter__(self):
        return iter(self._items)

    def sort_by(self, key_func: Callable[[Any], Any], reverse: bool = False):
        """Сортирует коллекцию по ключу (стратегия сортировки)."""
        self._items.sort(key=key_func, reverse=reverse)
        return self   # для цепочек

    def filter_by(self, predicate: Callable[[Any], bool]):
        """Фильтрует коллекцию, оставляя только элементы, удовлетворяющие предикату."""
        self._items = list(filter(predicate, self._items))
        return self

    def apply(self, func: Callable[[Any], Any]):
        """Применяет функцию ко всем элементам коллекции (стратегия обработки)."""
        self._items = [func(item) for item in self._items]
        return self

    def map(self, func: Callable[[Any], Any]):
        """Применяет функцию и возвращает новую коллекцию из результатов."""
        return AdvancedCollection([func(item) for item in self._items])

    def to_list(self):
        return self._items.copy()

    def __str__(self):
        return '\n'.join(str(item) for item in self._items)