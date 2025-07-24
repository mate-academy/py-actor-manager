from managers import ActorManager

if __name__ == "__main__":
    manager = ActorManager("library_db.sqlite", "actors")

    manager.create("Leonardo", "DiCaprio")
    manager.create("Natalie", "Portman")

    print("All actors: ")
    for actor in manager.all():
        print(actor)

    manager.update(1, "Leo", "Dicaprio")

    manager.delete(2)

    print("After updates: ")
    for actor in manager.all():
        print(actor)
