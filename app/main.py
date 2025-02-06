from models import Actor
from managers import ActorManager


# if __name__ == "__main__":
#     Actor.objects = ActorManager()

#     Actor.objects.create(first_name="Emma", last_name="Watson")
#     Actor.objects.create(first_name="Daniel", last_name="Radclife")
#     print(Actor.objects.all())
#     Actor.objects.update(2, "Daniel", "Radcliffe")
#     print(Actor.objects.all())
#     Actor.objects.delete(1)
#     print(Actor.objects.all())

def main():
    db_path = "cinema.db"
    manager = ActorManager(db_path)

    manager.create("John", "Doe")
    manager.create("Jane", "Smith")

    actors = manager.all()
    for actor in actors:
        print(actor)
    