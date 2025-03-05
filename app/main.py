from models import Actor
from managers import ActorManager

if __name__ == "__main__":
    manager = ActorManager()

    manager.create(Actor(id=1, first_name="Emma", last_name="Watson"))
    manager.create(Actor(id=2, first_name="Daniel", last_name="Radcliffe"))

    print(manager.all())

    manager.update(2, "Daniel", "Radcliffe-Updated")
    print(manager.all())

    manager.delete(1)
    print(manager.all())
