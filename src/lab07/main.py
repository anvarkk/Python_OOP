import sys
from app import BookApp
from cli import ConsoleUI
from storage import save, load

DATA_FILE = "books.json"

def main() -> None:
    """Загружает данные, создаёт приложение и запускает интерфейс."""
    # Загрузка
    books = load(DATA_FILE)
    app = BookApp()
    app.load_books(books)

    # Запуск UI
    ui = ConsoleUI(app)
    try:
        ui.run()
    finally:
        # Сохранение при выходе
        save(app.get_all(), DATA_FILE)
        print("Данные сохранены.")

if __name__ == "__main__":
    main()