from interfaces import Printable, Comparable   # <-- добавить эту строку
from models import Book, Magazine
from collection import MediaCollection

def main():
    print("=== Лабораторная работа №4: Интерфейсы и ABC (оценка 5) ===\n")

    # 1. Создаём объекты разных типов
    book1 = Book("1984", "George Orwell", 1949, 15.99)
    book2 = Book("Brave New World", "Aldous Huxley", 1932, 12.99)
    mag1 = Magazine("National Geographic", 345, "March", 2024, 5.99)
    mag2 = Magazine("Tech Today", 78, "April", 2024, 7.50)

    # 2. Коллекция
    coll = MediaCollection()
    coll.add(book1)
    coll.add(book2)
    coll.add(mag1)
    coll.add(mag2)

    # Сценарий 1: Полиморфный вызов to_string() через интерфейс Printable
    print("Сценарий 1: Вызов to_string() для всех Printable объектов")
    for item in coll.get_printable():
        print(f"  {item.to_string()}")
    print()

    # Сценарий 2: Сортировка через Comparable (книги по году, журналы по цене)
    print("Сценарий 2: Сортировка коллекции с помощью compare_to")
    coll.sort_by_comparable()
    print("  Отсортированные объекты:")
    for item in coll:
        print(f"    {item.to_string()}")
    print()

    # Сценарий 3: Фильтрация по интерфейсу (только Comparable)
    print("Сценарий 3: Фильтрация объектов, реализующих Comparable")
    comp_items = coll.get_comparable()
    for item in comp_items:
        print(f"  {item.to_string()} (реализует Comparable)")
    print()

    # Сценарий 4: Проверка через isinstance
    print("Сценарий 4: Проверка типов с помощью isinstance")
    print(f"  book1 является Printable? {isinstance(book1, Printable)}")
    print(f"  book1 является Comparable? {isinstance(book1, Comparable)}")
    print(f"  mag1 является Printable? {isinstance(mag1, Printable)}")
    print(f"  mag1 является Comparable? {isinstance(mag1, Comparable)}")
    print()

    # Сценарий 5: Универсальная функция печати (работа через интерфейс)
    print("Сценарий 5: Универсальная печать через интерфейс (coll.print_all())")
    coll.print_all()
    print()

    # Сценарий 6: Сравнение объектов (демонстрация compare_to)
    print("Сценарий 6: Сравнение книг по году (compare_to)")
    print(f"  {book1.title} ({book1.year}) vs {book2.title} ({book2.year}): {book1.compare_to(book2)}")
    print(f"  {mag1.title} (${mag1.price}) vs {mag2.title} (${mag2.price}): {mag1.compare_to(mag2)}")

if __name__ == "__main__":
    main()