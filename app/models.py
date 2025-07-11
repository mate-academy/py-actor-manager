from dataclasses import dataclass


@dataclass
class Actor:
    """Dataclass that represents actor entity."""

    id: int
    first_name: str
    last_name: str

