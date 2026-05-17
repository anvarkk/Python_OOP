class DuplicateItemError(Exception):
    """Объект с таким идентификатором уже существует."""
    pass

class ItemNotFoundError(Exception):
    """Объект не найден в коллекции."""
    pass

class InvalidInputError(Exception):
    """Некорректный ввод пользователя."""
    pass