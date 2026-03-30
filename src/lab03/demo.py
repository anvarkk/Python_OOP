from book import Book
from magazine import Magazine
from media_collection import MediaCollection

def main():
    print("=== Демонстрация полиморфизма (Lab03) ===\n")
    
    # 1. Создаём объекты разных типов
    book1 = Book("1984", "George Orwell", 1949, 15.99)
    book2 = Book("The Great Gatsby", "F. Scott Fitzgerald", 1925, 12.50)
    magazine1 = Magazine("National Geographic", 345, "Март", 2024, 5.99)
    magazine2 = Magazine("Tech Today", 78, "Апрель", 2024, 7.50)
    
    # 2. Создаём коллекцию и добавляем объекты
    collection = MediaCollection()
    collection.add(book1)
    collection.add(book2)
    collection.add(magazine1)
    collection.add(magazine2)
    
    print("Все объекты в коллекции (полиморфный вызов get_info):")
    for item in collection:
        print(f"  {item.get_info()}")  # полиморфный метод
    
    # 3. Проверка типов через isinstance
    print("\nПроверка типов объектов с помощью isinstance():")
    for item in collection:
        if isinstance(item, Book):
            print(f"  {item.title} — это книга, автор: {item.author}")
        elif isinstance(item, Magazine):
            print(f"  {item.title} — это журнал, выпуск №{item.issue_number}")
    
    # 4. Поиск по названию
    print("\nПоиск по названию '1984':")
    found = collection.find_by_title("1984")
    for item in found:
        print(f"  {item.get_info()}")
    
    # 5. Попытка добавить дубликат
    print("\nПопытка добавить дубликат книги:")
    try:
        collection.add(book1)
    except ValueError as e:
        print(f"  Ошибка: {e}")
    
    # 6. Демонстрация удаления
    print("\nУдаляем журнал 'Tech Today':")
    collection.remove(magazine2)
    print(f"  Осталось объектов: {len(collection)}")
    
    # 7. Изменение цены через setter (полиморфизм свойств)
    print("\nИзменяем цену книги '1984':")
    print(f"  Старая цена: {book1.price:.2f} руб.")
    book1.price = 18.99
    print(f"  Новая цена: {book1.price:.2f} руб.")
    
    # 8. Вызов бизнес-методов специфичных для класса
    print("\nПрименяем скидку 10% к книге '1984':")
    book1.apply_discount(10)
    print(f"  Цена после скидки: {book1.price:.2f} руб.")
    
    print("\nПрименяем сезонную скидку 20% к журналу 'National Geographic':")
    magazine1.apply_seasonal_discount(20)
    print(f"  Цена после скидки: {magazine1.price:.2f} руб.")
    
    # 9. Использование __len__ и __iter__
    print(f"\nВсего элементов в коллекции: {len(collection)}")
    print("Перебор коллекции (__iter__):")
    for idx, item in enumerate(collection, 1):
        print(f"  {idx}. {item.get_info()}")

if __name__ == "__main__":
    main()