from model import Book

def main():
    print("=== Демонстрация работы класса Book (оценка 5) ===\n")

    # Сценарий 1: создание книг и отображение статуса
    print("1. Создаём две книги:")
    book1 = Book("1984", "Джордж Оруэлл", 1949, 500.0)
    book2 = Book("Мастер и Маргарита", "Михаил Булгаков", 1967, 650.0)
    print(book1)
    print(book2)
    print()

    # Сценарий 2: выдача книги (изменение состояния)
    print("2. Выдаём первую книгу:")
    book1.check_out()
    print(book1)
    print("\nПытаемся выдать её же повторно:")
    book1.check_out()
    print()

    # Сценарий 3: возврат книги в хорошем состоянии
    print("3. Возвращаем первую книгу без повреждений:")
    book1.return_book()
    print(book1)
    print()

    # Сценарий 4: выдача, возврат с повреждением и ремонт
    print("4. Выдаём вторую книгу, возвращаем повреждённой, затем ремонтируем:")
    book2.check_out()
    book2.return_book(damaged=True)
    print(book2)
    print("\nПытаемся выдать повреждённую книгу:")
    book2.check_out()
    print("\nРемонтируем:")
    book2.repair()
    print(book2)
    print()

    # Сценарий 5: проверка валидации (ошибки)
    print("5. Проверка валидации (ошибки):")
    try:
        bad_book = Book("", "Автор", 2000, 100)
    except ValueError as e:
        print(f"Ошибка названия: {e}")
    try:
        bad_book = Book("Книга", "Автор", 3000, 100)
    except ValueError as e:
        print(f"Ошибка года: {e}")
    try:
        bad_book = Book("Книга", "Автор", 2000, -10)
    except ValueError as e:
        print(f"Ошибка цены: {e}")
    print()

    # Дополнительно: сравнение и бизнес-методы
    print("6. Сравнение книг и применение скидки:")
    book3 = Book("1984", "Джордж Оруэлл", 1949, 500.0)
    print(f"book1 == book3? {book1 == book3}")
    print(f"Цена book3 до скидки: {book3.price:.2f}")
    book3.apply_discount(10)
    print(f"После скидки 10%: {book3.price:.2f}")
    print(f"Современная ли книга? {book3.is_modern()}")
    print()

    print(f"Всего создано книг: {Book.get_total_books()}")

if __name__ == "__main__":
    main()