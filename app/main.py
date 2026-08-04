from app.managers import ActorManager


def main() -> None:
    manager = ActorManager(db_name="cinema.db", table_name="actors")

    manager.create("Kianu", "Reeves")
    manager.create("Scarlett", "Johansson")
    print("After create:", manager.all())

    manager.update(1, "Keanu", "Reeves")
    print("After update:", manager.all())

    manager.delete(2)
    print("After delete:", manager.all())


if __name__ == "__main__":
    main()
