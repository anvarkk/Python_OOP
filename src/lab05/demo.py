from models import Book, Magazine
from strategies import (
    by_title, by_year, by_price, by_title_then_year,
    is_book, is_magazine, price_less_than, year_after,
    apply_discount, to_string, PriceIncrease
)
from collection import AdvancedCollection

def main():
    print("=== Лабораторная работа №5: Стратегии и делегаты (оценка 5) ===\n")

    # Создаём объекты
    books = [
        Book("1984", "Orwell", 1949, 15.99),
        Book("Brave New World", "Huxley", 1932, 12.99),
        Book("Fahrenheit 451", "Bradbury", 1953, 14.99)
    ]
    magazines = [
        Magazine("National Geographic", 345, 2024, 5.99),
        Magazine("Tech Today", 78, 2024, 7.50),
        Magazine("Science", 102, 2023, 9.99)
    ]
    coll = AdvancedCollection(books + magazines)

    print("Исходная коллекция:")
    print(coll)
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 1: цепочка filter -> sort -> apply с выводом на каждом шаге
    print("СЦЕНАРИЙ 1: Цепочка операций (фильтр по цене <= 10, сортировка по году, скидка 10%)")
    result = (AdvancedCollection(coll.to_list())
              .filter_by(price_less_than(10))
              .sort_by(by_year)
              .apply(apply_discount(10)))
    print("Результат цепочки:")
    print(result)
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 2: Замена стратегии сортировки без изменения кода коллекции
    print("СЦЕНАРИЙ 2: Сортировка тремя разными стратегиями")
    coll2 = AdvancedCollection(books + magazines[:1])
    print("По названию (by_title):")
    print(coll2.sort_by(by_title))
    print("\nПо цене (by_price):")
    print(coll2.sort_by(by_price))
    print("\nПо году и названию (by_title_then_year):")
    print(coll2.sort_by(by_title_then_year))
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 3: Фильтрация двумя функциями (is_book и year_after)
    print("СЦЕНАРИЙ 3: Фильтрация")
    coll3 = AdvancedCollection(books + magazines)
    print("Только книги:")
    print(coll3.filter_by(is_book))
    print("\nТолько объекты после 2000 года:")
    print(coll3.filter_by(year_after(2000)))
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 4: Применение map для преобразования
    print("СЦЕНАРИЙ 4: map (преобразование в строки и извлечение названий)")
    coll4 = AdvancedCollection(books)
    strings = coll4.map(to_string)
    print("Результат map(to_string):")
    print(strings)
    titles = coll4.map(lambda x: x.title)
    print("\nРезультат map(lambda x: x.title):")
    print(titles)
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 5: Callable-объект как стратегия (PriceIncrease)
    print("СЦЕНАРИЙ 5: Применение callable-стратегии PriceIncrease")
    coll5 = AdvancedCollection([Book("Test", "Author", 2000, 10.00)])
    print("До применения:", coll5)
    coll5.apply(PriceIncrease(20))   # увеличить цену на 20%
    print("После увеличения на 20%:", coll5)
    print("\n" + "="*50 + "\n")

    # СЦЕНАРИЙ 6: Использование lambda для простых операций
    print("СЦЕНАРИЙ 6: Лямбда-функции для сортировки и фильтрации")
    coll6 = AdvancedCollection(books)
    coll6.sort_by(lambda x: x.price, reverse=True)
    print("Сортировка по цене (убывание) через lambda:")
    print(coll6)
    coll6.filter_by(lambda x: x.year > 1940)
    print("Фильтрация (год > 1940) через lambda:")
    print(coll6)

if __name__ == "__main__":
    main()