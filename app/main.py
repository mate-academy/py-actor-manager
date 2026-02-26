from app.models import Actor
from app.managers import ActorManager


def run_demo() -> None:
    # Changed table_name to "actors" (plural) as requested
    manager = ActorManager("cinema_db.sqlite", "actors")
    Actor.objects = manager

    print("Adding actors...")
    Actor.objects.create(first_name="Leonardo", last_name="DiCaprio")
    Actor.objects.create(first_name="Cate", last_name="Blanchett")

    print("\nList of actors in the database:")
    for actor in Actor.objects.all():
        print(f"- {actor.first_name} {actor.last_name} (ID: {actor.id})")


if __name__ == "__main__":
    run_demo()
