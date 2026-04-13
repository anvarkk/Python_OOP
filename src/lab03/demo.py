from book import Book
from magazine import Magazine
from media_collection import MediaCollection

def main():
    print("=== Лабораторная работа №3 (оценка 5) – Полиморфизм и фильтрация ===\n")

    # 1. Создаём разные объекты
    book1 = Book("1984", "Джордж Оруэлл", 1949, 500.0)
    book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 650.0)
    mag1 = Magazine("Наука и жизнь", 345, "Март", 2024, 150.0)
    mag2 = Magazine("Tech Today", 78, "Апрель", 2024, 200.0)

    # 2. Единый список объектов (коллекция)
    collection = MediaCollection()
    collection.add(book1)
    collection.add(book2)
    collection.add(mag1)
    collection.add(mag2)

    # 3. Полиморфизм: вызываем один и тот же метод get_info() для всех
    print("▶ Полиморфный вывод всех объектов (метод get_info()):")
    for item in collection:
        print(f"  {item.get_info()}")   # разное поведение без проверки типов
    print()

    # 4. Фильтрация по типу: только книги
    print("▶ Только книги (фильтрация):")
    for book in collection.get_books():
        print(f"  {book.get_info()}")
    print()

    # 5. Фильтрация по типу: только журналы
    print("▶ Только журналы (фильтрация):")
    for mag in collection.get_magazines():
        print(f"  {mag.get_info()}")
    print()

    # 6. Сценарий: применение скидки к книгам (свой метод)
    print("▶ Применяем скидку 10% ко всем книгам:")
    for book in collection.get_books():
        old_price = book.price
        book.apply_discount(10)
        print(f"  {book.title}: {old_price:.2f} → {book.price:.2f} руб.")
    print()

    # 7. Сценарий: сезонная скидка на журналы
    print("▶ Сезонная скидка 15% на журналы:")
    for mag in collection.get_magazines():
        old_price = mag.price
        mag.apply_seasonal_discount(15)
        print(f"  {mag.title}: {old_price:.2f} → {mag.price:.2f} руб.")
    print()

    # 8. Сценарий: поиск по названию (работает для любых медиа)
    print("▶ Поиск по названию '1984':")
    found = collection.find_by_title("1984")
    for item in found:
        print(f"  {item.get_info()}")
    print()

    # 9. Итог: количество объектов
    print(f"Всего объектов в коллекции: {len(collection)}")
    print(f"Из них книг: {len(collection.get_books())}, журналов: {len(collection.get_magazines())}")

if __name__ == "__main__":
    main()