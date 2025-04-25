from typing import List
from models import Actor
from managers import ActorManager


def display_actors(title: str, actors: List[Actor]) -> None:
    print(f"\n{title}: ")
    for actor in actors:
        print(f"{actor.id}: {actor.first_name} {actor.last_name}")


def main() -> None:
    # Initialize manager (creates DB connection)
    manager = ActorManager()

    # Create some actors
    print("Creating actors...")
    manager.create("Tom", "Hanks")
    manager.create("Meryl", "Streep")
    manager.create("Leonardo", "DiCaprio")

    # Display all actors
    actors = manager.all()
    display_actors("Initial Actors", actors)

    # Update first actor
    print("\nUpdating first actor...")
    manager.update(1, "Thomas", "Hanks")

    # Display after update
    display_actors("After Update", manager.all())

    # Delete second actor
    print("\nDeleting second actor...")
    manager.delete(2)

    # Display after deletion
    display_actors("After Deletion", manager.all())


if __name__ == "__main__":
    main()
# if __name__ == "__main__":
#     Actor.objects = ActorManager()
#
#     Actor.objects.create(first_name="Emma", last_name="Watson")
#     Actor.objects.create(first_name="Daniel", last_name="Radclife")
#     print(Actor.objects.all())
#     Actor.objects.update(2, "Daniel", "Radcliffe")
#     print(Actor.objects.all())
#     Actor.objects.delete(1)
#     print(Actor.objects.all())
