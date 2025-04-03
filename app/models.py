from dataclasses import dataclass


@dataclass
class Actor:
    first_name: str
    last_name: str
    id: int = None