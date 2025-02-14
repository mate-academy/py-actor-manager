from models import Actor  # noqa: F401
from managers import ActorManager


def main() -> None:
    actor_manager = ActorManager()
    actor_manager.create_table()

    try:
        actor_id_emma = actor_manager.create(first_name="Emma",
                                             last_name="Watson")
        actor_id_daniel = actor_manager.create(first_name="Daniel",
                                               last_name="Radcliffe")

        if actor_id_emma and actor_id_daniel:
            print("Актори успішно створені.")

        print("Всі актори:")
        for actor in actor_manager.all():
            print(actor)

        if actor_id_daniel:
            if actor_manager.update(actor_id_daniel, first_name="Daniel",
                                    last_name="Radcliffe"):
                print("Актор успішно оновлений.")
                print("Всі актори після оновлення:")
                for actor in actor_manager.all():
                    print(actor)

        if actor_id_emma:
            if actor_manager.delete(actor_id_emma):
                print("Актор успішно видалений.")
            else:
                print("Не вдалося видалити актора.")
        else:
            print("Не вдалося знайти актора для видалення.")

        print("Всі актори після видалення:")
        for actor in actor_manager.all():
            print(actor)

    except Exception as e:
        print(f"Виникла помилка: {e}")
    finally:
        actor_manager.close()


if __name__ == "__main__":
    main()
