from dataclasses import dataclass
from typing import TypedDict


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str


class ActorData(TypedDict):
    first_name: str
    last_name: str

# add dataclass here
