from model import Book

def main():
    print("=== Демонстрация работы класса Book ===\n")

    # 1. Создание объектов
    book1 = Book("1984", "George Orwell", 1949, 15.99)
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 12.50)
    book3 = Book("To Kill a Mockingbird", "Harper Lee", 1960, 14.95)

    # 2. Вывод через print (__str__)
    print("Созданные книги:")
    print(book1)
    print(book2)
    print(book3)
    print()

    # 3. Сравнение двух объектов (__eq__)
    book4 = Book("1984", "George Orwell", 1949, 15.99)
    print(f"Сравнение book1 и book4 (одинаковые): {book1 == book4}")
    print(f"Сравнение book1 и book2 (разные): {book1 == book2}")
    print()

    # 4. Пример некорректного создания (через try/except)
    print("Попытка создать книгу с некорректными данными:")
    try:
        bad_book = Book("", "Unknown", 2000, 10.0)  # Пустое название
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        bad_book = Book("Title", "Author", 1800, -5.0)  # Отрицательная цена
    except ValueError as e:
        print(f"Ошибка: {e}")

    try:
        bad_book = Book("Title", "Author", 3000, 10.0)  # Год вне диапазона
    except ValueError as e:
        print(f"Ошибка: {e}")
    print()

    # 5. Изменение свойства через setter с валидацией
    print("Изменение цены и года через setter:")
    print(f"Исходная цена книги '{book1.title}': ${book1.price:.2f}")
    book1.price = 18.99
    print(f"Новая цена: ${book1.price:.2f}")
    try:
        book1.price = -5.0  # Попытка установить отрицательную цену
    except ValueError as e:
        print(f"Ошибка при установке цены: {e}")

    print(f"Исходный год книги '{book2.title}': {book2.year}")
    book2.year = 2005
    print(f"Новый год: {book2.year}")
    try:
        book2.year = 1000  # Попытка установить некорректный год
    except ValueError as e:
        print(f"Ошибка при установке года: {e}")
    print()

    # 6. Бизнес-методы
    print("Применение скидки:")
    print(f"Цена книги '{book3.title}': ${book3.price:.2f}")
    book3.apply_discount(10)  # скидка 10%
    print(f"Цена после скидки 10%: ${book3.price:.2f}")
    try:
        book3.apply_discount(150)  # некорректная скидка
    except ValueError as e:
        print(f"Ошибка при применении скидки: {e}")
    print()

    print("Проверка на современность:")
    print(f"Книга '{book1.title}' ({book1.year}) современная? {book1.is_modern()}")
    print(f"Книга '{book2.title}' ({book2.year}) современная? {book2.is_modern()}")
    print(f"Книга '{book3.title}' ({book3.year}) современная? {book3.is_modern()}")
    print()

    # 7. Атрибут класса total_books
    print("Атрибут класса total_books (количество созданных книг):")
    print(f"Через класс: Book.total_books = {Book.total_books}")
    print(f"Через экземпляр: book1.total_books = {book1.total_books}")
    print(f"Через метод класса: Book.get_total_books() = {Book.get_total_books()}")
    print()

    # 8. Дополнительно: вывод __repr__
    print("Представление __repr__ для book1:")
    print(repr(book1))

if __name__ == "__main__":
    main()