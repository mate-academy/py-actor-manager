from managers import ActorManager


def main() -> None:
    manager = ActorManager()

    manager.create("Emma", "Watson")
    manager.create("Daniel", "Radcliffe")

    print(manager.all())

    manager.update(2, "Daniel", "Radcliffe")

    print(manager.all())

    manager.delete(1)

    print(manager.all())

if __name__ == "__main__":
    main()