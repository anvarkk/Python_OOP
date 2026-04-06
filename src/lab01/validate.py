def validate_title(title):
    if not isinstance(title, str) or not title.strip():
        raise ValueError("Название книги должно быть непустой строкой.")
    return title.strip()

def validate_author(author):
    if not isinstance(author, str) or not author.strip():
        raise ValueError("Имя автора должно быть непустой строкой.")
    return author.strip()

def validate_year(year):
    if not isinstance(year, int) or year < 1440 or year > 2025:
        raise ValueError("Год издания должен быть целым числом от 1440 до 2025.")
    return year

def validate_price(price):
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Цена должна быть положительным числом.")
    return float(price)