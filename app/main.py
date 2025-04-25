from managers import ActorManager


def main() -> None:
    manager = ActorManager()

    # Criando atores
    actor1 = manager.create("Robert", "Downey")
    actor2 = manager.create("Scarlett", "Johansson")
    print(actor1)
    print(actor2)

    # Listando todos
    print("\nTodos os atores:")
    for actor in manager.all():
        print(actor)

    # Atualizando
    print("\nAtualizando ator de ID 1:")
    manager.update(1, first_name="Rob", last_name="Downey Jr.")

    # Após atualização
    print("\nAtores após atualização:")
    for actor in manager.all():
        print(actor)

    # Deletando
    print("\nDeletando ator de ID 2:")
    manager.delete(2)

    # Final
    print("\nAtores finais:")
    for actor in manager.all():
        print(actor)


if __name__ == "__main__":
    main()
