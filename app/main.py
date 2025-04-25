from typing import List, Optional
from managers import ActorManager
from models import Actor


def display_actors(title: str, actors: List[Actor]) -> None:
    """Display a list of actors with a title.

    Args:
        title: The header to display before the list
        actors: List of Actor objects to display
    """
    print(f"\n{title}: ")
    for actor in actors:
        print(f"{actor.id}: {actor.first_name} {actor.last_name}")


def get_actor_by_name(
        actors: List[Actor],
        first_name: str,
        last_name: str) -> Optional[Actor]:
    """Helper function to find an actor by name."""
    for actor in actors:
        if actor.first_name == first_name and actor.last_name == last_name:
            return actor
    return None


def main() -> None:
    """Main function to test ActorManager functionality."""
    # Initialize manager (creates DB connection)
    manager = ActorManager()

    # Clear any existing data for clean testing
    for actor in manager.all():
        manager.delete(actor.id)

    # Create some actors and store their IDs
    print("Creating actors...")
    manager.create("Tom", "Hanks")
    manager.create("Meryl", "Streep")
    manager.create("Leonardo", "DiCaprio")

    # Get all actors and find them by name
    actors = manager.all()
    tom = get_actor_by_name(actors, "Tom", "Hanks")
    meryl = get_actor_by_name(actors, "Meryl", "Streep")
    leo = get_actor_by_name(actors, "Leonardo", "DiCaprio")

    # Verify we found all actors
    if not all([tom, meryl, leo]):
        print("Error: Not all actors were created successfully!")
        return

    # Display all actors
    display_actors("Initial Actors", actors)

    # Update first actor using the found ID
    print("\nUpdating first actor...")
    manager.update(tom.id, "Thomas", "Hanks")

    # Display after update
    display_actors("After Update", manager.all())

    # Delete second actor using the found ID
    print("\nDeleting second actor...")
    manager.delete(meryl.id)

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
