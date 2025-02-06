from app.managers import ActorManager

if __name__ == "__main__":
    manager = ActorManager()

    # Create actors
    actor1 = manager.create("Leonardo", "DiCaprio")
    actor2 = manager.create("Johnny", "Depp")

    print("Added actors:")
    for actor in manager.all():
        print(actor)

    # Update actor data
    manager.update(actor1.id, "Leonardo", "DiCaprio Updated")

    print("\nAfter update:")
    for actor in manager.all():
        print(actor)

    # Delete an actor
    manager.delete(actor2.id)

    print("\nAfter deletion:")
    for actor in manager.all():
        print(actor)
