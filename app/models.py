from dataclasses import dataclass


@dataclass
class Actor:
    id: int | None
    first_name: str
    last_name: str
