# main.py
from models import Actor
from managers import ActorManager


def main() -> None:
    """Основная функция для тестирования функциональности."""
    # Инициализация менеджера
    Actor.objects = ActorManager()

    # Создание актеров
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")

    # Получение всех актеров и вывод
    print("All actors after creation:")
    print(Actor.objects.all())

    # Обновление актера с id=2
    Actor.objects.update(2, "Daniel", "Radcliffe")

    # Получение всех актеров после обновления и вывод
    print("All actors after update:")
    print(Actor.objects.all())

    # Удаление актера с id=1
    Actor.objects.delete(1)

    # Получение всех актеров после удаления и вывод
    print("All actors after deletion:")
    print(Actor.objects.all())


if __name__ == "__main__":
    main()
