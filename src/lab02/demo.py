from model import Book
from collection import Library

def main():
    print("=== Демонстрация работы библиотеки (Lab02) ===\n")

    # 1. Создаём несколько книг
    book1 = Book("1984", "George Orwell", 1949, 15.99)
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 12.50)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 14.95)
    book4 = Book("1984", "George Orwell", 1949, 15.99)   # дубликат book1

    # 2. Создаём библиотеку и добавляем книги
    lib = Library()
    lib.add(book1)
    lib.add(book2)
    lib.add(book3)
    print("После добавления трёх книг:")
    for book in lib:
        print(book)

    # 3. Попытка добавить дубликат
    print("\nПопытка добавить дубликат (book4):")
    try:
        lib.add(book4)
    except ValueError as e:
        print(f"Ошибка: {e}")

    # 4. Проверка ограничения типа
    print("\nПопытка добавить не-книгу:")
    try:
        lib.add("not a book")
    except TypeError as e:
        print(f"Ошибка: {e}")

    # 5. Удаление книги
    print("\nУдаляем книгу book2...")
    lib.remove(book2)
    print("Книги после удаления:")
    for book in lib:
        print(book)

    # 6. Поиск по названию
    print("\nПоиск книг с названием '1984':")
    found = lib.find_by_title("1984")
    for book in found:
        print(book)

    # 7. Поиск по автору
    print("\nПоиск книг автора 'Harper Lee':")
    found = lib.find_by_author("Harper Lee")
    for book in found:
        print(book)

    # 8. Использование len()
    print(f"\nВ библиотеке сейчас {len(lib)} книг.")

    # 9. Итерация через for (демонстрация __iter__)
    print("\nВсе книги библиотеки (через for):")
    for idx, book in enumerate(lib, 1):
        print(f"{idx}. {book}")

    # 10. Использование get_all()
    print("\nКопия всех книг через get_all():")
    all_books = lib.get_all()
    for book in all_books:
        print(book)

if __name__ == "__main__":
    main()