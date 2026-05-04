# Функции сортировки (стратегии)
def by_title(item):
    return item.title

def by_year(item):
    return item.year

def by_price(item):
    return item.price

def by_title_then_year(item):
    return (item.title, item.year)

# Функции фильтрации
def is_book(item):
    return isinstance(item, Book)

def is_magazine(item):
    return isinstance(item, Magazine)

def price_less_than(max_price):
    """Фабрика функций: возвращает функцию-фильтр."""
    def filter_fn(item):
        return item.price <= max_price
    return filter_fn

def year_after(min_year):
    def filter_fn(item):
        return item.year >= min_year
    return filter_fn

# Функции преобразования (для map)
def apply_discount(percent):
    """Возвращает функцию, уменьшающую цену объекта на percent%."""
    def discount_fn(item):
        item._price = item.price * (1 - percent / 100)
        return item
    return discount_fn

def to_string(item):
    return str(item)

# Callable-объект для паттерна Стратегия
class PriceIncrease:
    """Стратегия: увеличивает цену на заданный процент."""
    def __init__(self, percent):
        self.percent = percent
    def __call__(self, item):
        item._price = item.price * (1 + self.percent / 100)
        return item