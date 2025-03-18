from app.managers import ActorManager


def main() -> None:
    manager = ActorManager("cinema.db")

    # Очищення таблиці перед тестами
    manager.clear_table()
    print("Таблиця очищена.")
    print("Стан бази даних після очищення:")
    print(manager.all())  # Має показати порожній список

    # Створення акторів
    actor_id1 = manager.create("Tom", "Hanks")
    actor_id2 = manager.create("Meryl", "Streep")

    print("\nВсі актори після створення:")
    actors = manager.all()
    for actor in actors:
        print(actor)

    # Оновлення актора
    manager.update(actor_id1, "Thomas", "Hanks")
    print("\nСтан бази після оновлення актора (id=1):")
    for actor in manager.all():
        print(actor)

    # Видалення актора
    manager.delete(actor_id2)
    print("\nСтан бази після видалення актора (id=2):")
    actors = manager.all()
    for actor in actors:
        print(actor)

    # Закриття з'єднання
    manager.close()


if __name__ == "__main__":
    main()
