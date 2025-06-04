from typing import List
from app.models import Actor


class ActorManager:
    def __init__(self, db_name: str, table_name: str) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._data = []
        self._next_id = 1

    def create(self, first_name: str,
               last_name: str) -> None:
        actor = Actor(id=self._next_id,
                      first_name=first_name,
                      last_name=last_name)
        self._data.append(actor)
        self._next_id += 1

    def all(self) -> List[Actor]:
        return list(self._data)

    def update(self, pk: int, new_first_name: str,
               new_last_name: str) -> None:
        for i, actor in enumerate(self._data):
            if actor.id == pk:
                self._data[i] = Actor(id=pk,
                                      first_name=new_first_name,
                                      last_name=new_last_name)
                return

    def delete(self, pk: int) -> None:
        self._data = [actor for actor in self._data if actor.id != pk]
