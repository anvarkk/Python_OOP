from typing import List, Callable, Optional
from models import Book
from app import BookApp
from exceptions import DuplicateItemError, ItemNotFoundError, InvalidInputError

class ConsoleUI:
    """Класс для управления пользовательским интерфейсом."""

    def __init__(self, app: BookApp) -> None:
        self.app = app

    def display_menu(self) -> None:
        """Выводит главное меню."""
        print("\n" + "=" * 40)
        print("          БИБЛИОТЕКА - ГЛАВНОЕ МЕНЮ")
        print("=" * 40)
        print("1. Добавить книгу")
        print("2. Показать все книги")
        print("3. Найти книгу по названию")
        print("4. Удалить книгу")
        print("5. Фильтровать книги (по цене <= заданной)")
        print("6. Сортировать книги")
        print("0. Выход")
        print("-" * 40)

    def get_choice(self) -> int:
        """Запрашивает у пользователя пункт меню с обработкой ошибок."""
        while True:
            try:
                choice = int(input("Ваш выбор: "))
                return choice
            except ValueError:
                print("Ошибка: введите число от 0 до 6.")

    def add_book_ui(self) -> None:
        """UI для добавления книги."""
        print("\n--- Добавление новой книги ---")
        try:
            title = input("Название: ").strip()
            if not title:
                raise InvalidInputError("Название не может быть пустым.")
            author = input("Автор: ").strip()
            if not author:
                raise InvalidInputError("Автор не может быть пустым.")
            year = self._input_int("Год издания: ", min_val=1440, max_val=2025)
            price = self._input_float("Цена (руб.): ", min_val=0.01)

            book = Book(title, author, year, price)
            self.app.add(book)
            print(f"✓ Книга '{title}' успешно добавлена.")
        except (DuplicateItemError, InvalidInputError) as e:
            print(f"Ошибка: {e}")
        except Exception as e:
            print(f"Непредвиденная ошибка: {e}")

    def show_all_ui(self) -> None:
        """UI для отображения всех книг."""
        books = self.app.get_all()
        if not books:
            print("\n--- Библиотека пуста ---")
        else:
            print("\n--- Список всех книг ---")
            self._print_table(books)

    def find_book_ui(self) -> None:
        """UI для поиска книги по названию."""
        print("\n--- Поиск книги ---")
        title = input("Введите название: ").strip()
        book = self.app.find(title)
        if book:
            print("\nНайдена книга:")
            print(f"  {book}")
        else:
            print(f"Книга '{title}' не найдена.")

    def remove_book_ui(self) -> None:
        """UI для удаления книги с подтверждением."""
        print("\n--- Удаление книги ---")
        title = input("Введите название удаляемой книги: ").strip()
        book = self.app.find(title)
        if not book:
            print(f"Книга '{title}' не найдена.")
            return

        print(f"Вы собираетесь удалить: {book}")
        confirm = input("Подтверждаете удаление? (y/n): ").strip().lower()
        if confirm == 'y':
            try:
                self.app.remove(title)
                print(f"✓ Книга '{title}' удалена.")
            except ItemNotFoundError as e:
                print(f"Ошибка: {e}")
        else:
            print("Удаление отменено.")

    def filter_ui(self) -> None:
        """UI для фильтрации книг (цена <= заданной)."""
        print("\n--- Фильтрация книг (цена <= ...) ---")
        try:
            max_price = self._input_float("Максимальная цена: ", min_val=0)
            filtered = self.app.filter(lambda b: b.price <= max_price)
            if filtered:
                print(f"\nКниги дешевле или равные {max_price:.2f} руб.:")
                self._print_table(filtered)
            else:
                print("Нет книг, удовлетворяющих условию.")
        except InvalidInputError as e:
            print(f"Ошибка: {e}")

    def sort_ui(self) -> None:
        """UI для сортировки с выбором стратегии."""
        print("\n--- Сортировка книг ---")
        print("1. По названию (А-Я)")
        print("2. По автору (А-Я)")
        print("3. По году (по возрастанию)")
        print("4. По цене (дешевле → дороже)")
        choice = self.get_choice()
        key_funcs = {
            1: lambda b: b.title,
            2: lambda b: b.author,
            3: lambda b: b.year,
            4: lambda b: b.price
        }
        if choice in key_funcs:
            sorted_books = self.app.sort(key_funcs[choice])
            print("\nОтсортированный список:")
            self._print_table(sorted_books)
        else:
            print("Неверный выбор сортировки.")

    def run(self) -> None:
        """Основной цикл приложения."""
        while True:
            self.display_menu()
            choice = self.get_choice()
            if choice == 0:
                print("До свидания!")
                break
            elif choice == 1:
                self.add_book_ui()
            elif choice == 2:
                self.show_all_ui()
            elif choice == 3:
                self.find_book_ui()
            elif choice == 4:
                self.remove_book_ui()
            elif choice == 5:
                self.filter_ui()
            elif choice == 6:
                self.sort_ui()
            else:
                print("Некорректный пункт. Выберите 0-6.")

    # Вспомогательные методы
    def _input_int(self, prompt: str, min_val: int = None, max_val: int = None) -> int:
        """Запрашивает целое число с проверкой границ."""
        while True:
            try:
                value = int(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Число должно быть не меньше {min_val}.")
                    continue
                if max_val is not None and value > max_val:
                    print(f"Число должно быть не больше {max_val}.")
                    continue
                return value
            except ValueError:
                print("Ошибка: введите целое число.")

    def _input_float(self, prompt: str, min_val: float = None) -> float:
        """Запрашивает вещественное число с проверкой минимума."""
        while True:
            try:
                value = float(input(prompt))
                if min_val is not None and value < min_val:
                    print(f"Число должно быть не меньше {min_val}.")
                    continue
                return value
            except ValueError:
                print("Ошибка: введите число.")

    def _print_table(self, books: List[Book]) -> None:
        """Выводит список книг в виде таблицы."""
        if not books:
            return
        # Определяем ширину столбцов
        titles = [b.title for b in books]
        authors = [b.author for b in books]
        years = [str(b.year) for b in books]
        prices = [f"{b.price:.2f}" for b in books]

        max_title = max(len(t) for t in titles) if titles else 10
        max_author = max(len(a) for a in authors) if authors else 10
        max_year = max(len(y) for y in years) if years else 4
        max_price = max(len(p) for p in prices) if prices else 6

        # Заголовок
        print(f"{'Название':<{max_title}} | {'Автор':<{max_author}} | {'Год':>{max_year}} | {'Цена, руб':>{max_price}}")
        print("-" * (max_title + max_author + max_year + max_price + 9))
        for b in books:
            print(f"{b.title:<{max_title}} | {b.author:<{max_author}} | {b.year:>{max_year}} | {b.price:>{max_price}.2f}")