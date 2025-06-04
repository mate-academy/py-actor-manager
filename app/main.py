from managers import ActorManager


if __name__ == "__main__":
    db = ActorManager()
    print(db.all())
