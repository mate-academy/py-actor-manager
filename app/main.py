from app.managers import ActorManager
from app.models import Actor

if __name__ == "__main__":
    Actor.objects = ActorManager(db_name="actors.db", table_name="actors")
    print(Actor.objects.all())
