from managers import ActorManager
from models import Actor


if __name__ == "__main__":
    manager = ActorManager("cinema.db")
    actor1_id = manager.create("Leonardo", "Dicaprio")
    actors = manager.all()
