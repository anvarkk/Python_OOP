from model import Book
from collection import Library

def main():
    print("=== Лабораторная работа №2 (оценка 5) – Коллекция объектов ===\n")

    # Сценарий 1: создание книг и добавление в библиотеку
    print("1. Создаём три книги и добавляем их в библиотеку:")
    book1 = Book("1984", "Джордж Оруэлл", 1949, 500.0)
    book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 650.0)
    book3 = Book("Преступление и наказание", "Фёдор Достоевский", 1866, 450.0)
    lib = Library()
    lib.add(book1)
    lib.add(book2)
    lib.add(book3)
    print("   Книги добавлены.")
    print(f"   В библиотеке {len(lib)} книг:")
    for book in lib:
        print(f"     {book}")
    print()

    # Сценарий 2: вывод всех книг через get_all()
    print("2. Получаем список всех книг (get_all()):")
    all_books = lib.get_all()
    for b in all_books:
        print(f"   {b}")
    print()

    # Сценарий 3: попытка добавить дубликат (отклоняется)
    print("3. Пытаемся добавить книгу-дубликат (та же '1984'):")
    book_dup = Book("1984", "Джордж Оруэлл", 1949, 500.0)
    try:
        lib.add(book_dup)
    except ValueError as e:
        print(f"   Ошибка (как и ожидалось): {e}")
    print()

    # Сценарий 4: удаление книги
    print("4. Удаляем книгу 'Преступление и наказание':")
    lib.remove(book3)
    print(f"   Осталось книг: {len(lib)}")
    for book in lib:
        print(f"     {book}")
    print()

    # Сценарий 5: поиск по названию
    print("5. Поиск книг по названию '1984':")
    found = lib.find_by_title("1984")
    for b in found:
        print(f"   {b}")
    print()

    # Сценарий 6: поиск по автору
    print("6. Поиск книг по автору 'Михаил Булгаков':")
    found = lib.find_by_author("Михаил Булгаков")
    for b in found:
        print(f"   {b}")
    print()

    # Сценарий 7: поиск по году
    print("7. Поиск книг по году 1949:")
    found = lib.find_by_year(1949)
    for b in found:
        print(f"   {b}")
    print()

    # Сценарий 8: итерация через for (__iter__)
    print("8. Итерация по библиотеке (for book in lib):")
    for idx, book in enumerate(lib, 1):
        print(f"   {idx}. {book}")
    print()

    # Сценарий 9: проверка ограничения типа (нельзя добавить строку)
    print("9. Попытка добавить объект не типа Book (строка):")
    try:
        lib.add("это не книга")
    except TypeError as e:
        print(f"   Ошибка: {e}")

if __name__ == "__main__":
    main()