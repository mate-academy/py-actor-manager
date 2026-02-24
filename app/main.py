from app.managers import ActorManager
from app.models import Actor

if __name__ == "__main__":
    Actor.objects = ActorManager("cinema.sqlite", "actors")
