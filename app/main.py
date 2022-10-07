from app.models import Actor
from app.managers import ActorManager

if __name__ == "__main__":
    Actor.objects = ActorManager()
