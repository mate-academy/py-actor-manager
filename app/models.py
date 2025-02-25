class Actor:
    def __init__(self, id: int, first_name: str, last_name: str):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Actor(id={self.id}, first_name='{self.first_name}', last_name='{self.last_name}')"