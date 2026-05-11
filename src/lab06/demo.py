from models import Book, Magazine
from container import TypedCollection, Displayable, Scorable, D, S

def main():
    print("=== Лабораторная работа №6: Generics и typing (оценка 5) ===\n")

    # ----- Часть 1: Аннотации и Generic (оценка 3) -----
    print("1. Создание типизированной коллекции (TypedCollection[Book]):")
    book_collection = TypedCollection[Book]()
    book1 = Book("1984", "Orwell", 1949, 15.99)
    book2 = Book("Brave New World", "Huxley", 1932, 12.99)
    book_collection.add(book1)
    book_collection.add(book2)
    print(f"Количество книг: {len(book_collection)}")
    print("Все книги:")
    for b in book_collection.get_all():
        print(f"  {b}")
    print()

    # Демонстрация валидации типов (при добавлении неверного типа IDE/статический анализатор поймает)
    # book_collection.add("не книга")  # ошибка типов

    # ----- Часть 2: find, filter, map (оценка 4) -----
    print("2. Метод find (поиск книги с годом > 1940):")
    found = book_collection.find(lambda b: b.year > 1940)
    print(f"  Найдено: {found}")
    not_found = book_collection.find(lambda b: b.year > 2000)
    print(f"  Не найдено: {not_found}")
    print()

    print("3. Метод filter (книги дешевле 14$):")
    cheap_books = book_collection.filter(lambda b: b.price < 14.0)
    for b in cheap_books:
        print(f"  {b}")
    print()

    print("4. Метод map (преобразование в названия и в цены):")
    titles = book_collection.map(lambda b: b.title)
    prices = book_collection.map(lambda b: b.price)
    print(f"  Названия: {titles}")
    print(f"  Цены: {prices}")
    print()

    # ----- Часть 3: Протоколы и bound TypeVar (оценка 5) -----
    print("5. TypedCollection с ограничением Displayable (показываем объекты, у которых есть display()):")
    displayable_collection = TypedCollection[D]()
    # Добавляем книгу и журнал – оба имеют метод display() без наследования от протокола
    displayable_collection.add(book1)
    displayable_collection.add(Magazine("National Geographic", 345, 2024, 5.99))
    displayable_collection.add(Magazine("Tech Today", 78, 2024, 7.50))
    print("Содержимое коллекции (вызов display()):")
    displayable_collection.display_all()
    print()

    print("6. TypedCollection с ограничением Scorable (объекты с методом score()):")
    scorable_collection = TypedCollection[S]()
    scorable_collection.add(book1)
    scorable_collection.add(book2)
    scorable_collection.add(Magazine("Science", 102, 2023, 9.99))
    # Вычислим сумму всех score:
    total_score = sum(scorable_collection.map(lambda x: x.score()))
    print(f"Суммарный score всех объектов: {total_score:.2f}")
    print("Объекты с их score:")
    for item in scorable_collection.get_all():
        print(f"  {item.display()} -> score = {item.score():.2f}")

if __name__ == "__main__":
    main()