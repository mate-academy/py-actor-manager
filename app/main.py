from models import Actor

if __name__ == "__main__":
    Actor.objects.create(first_name="Emma", last_name="Watson")
    Actor.objects.create(first_name="Daniel", last_name="Radclife")

    print("All Actors:")
    actors = Actor.objects.all()
    for actor in actors:
        print(f'{actor.id}: {actor.first_name} {actor.last_name}')

    Actor.objects.update(2, "Daniel", "Radcliffe")

    print("\nAfter Update:")
    actors = Actor.objects.all()
    for actor in actors:
        print(f"{actor.id}: {actor.first_name} {actor.last_name}")

    Actor.objects.delete(1)

    print("\nAfter Deletion:")
    actors = Actor.objects.all()
    for actor in actors:
        print(f"{actor.id}: {actor.first_name} {actor.last_name}")
