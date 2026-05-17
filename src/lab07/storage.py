import json
from typing import List
from models import Book

def save(collection: List[Book], filepath: str) -> None:
    """
    Сохраняет коллекцию книг в JSON-файл.

    Args:
        collection: Список книг.
        filepath: Путь к файлу.
    """
    data = [book.to_dict() for book in collection]
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def load(filepath: str) -> List[Book]:
    """
    Загружает коллекцию книг из JSON-файла.

    Args:
        filepath: Путь к файлу.

    Returns:
        Список книг.
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return [Book.from_dict(item) for item in data]
    except (FileNotFoundError, json.JSONDecodeError):
        return []