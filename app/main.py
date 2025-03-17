# main.py
from models import Actor
from managers import ActorManager


def main() -> None:
    """Основная функция для тестирования функциональности."""
    # Создание экземпляра менеджера
    manager = ActorManager()

    # Создание актеров
    actor1 = manager.create(first_name="Emma", last_name="Watson")
    actor2 = manager.create(first_name="Daniel", last_name="Radclife")

    # Получение всех актеров и вывод
    print("All actors after creation:")
    for actor in manager.all():
        print(actor)

    # Обновление актера с id=2
    updated_actor = manager.update(actor_id=actor2.id, first_name="Daniel", last_name="Radcliffe")
    print(f"Updated actor: {updated_actor}")

    # Удаление актера с id=1
    manager.delete(actor_id=actor1.id)
    print(f"Deleted actor with id: {actor1.id}")

    # Получение всех актеров после удаления и вывод
    print("All actors after deletion:")
    for actor in manager.all():
        print(actor)


if __name__ == "__main__":
    main()
