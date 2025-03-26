from models import Actors
from managers import ActorsManager

if __name__ == "__main__":
    Actors.objects = ActorsManager()

    Actors.objects.create(first_name="Emma", last_name="Watson")
    Actors.objects.create(first_name="Daniel", last_name="Radclife")
    print(Actors.objects.all())
    Actors.objects.update(2, "Daniel", "Radcliffe")
    print(Actors.objects.all())
    Actors.objects.delete(1)
    print(Actors.objects.all())
