from dataclasses import dataclass


@dataclass(frozen=True)
class Actor:
    id: int
    first_name: str
    last_name: str
