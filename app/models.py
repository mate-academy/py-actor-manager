from dataclasses import dataclass


@dataclass
class Actor:
    """Dataclass representing an actor entity."""
    id: int
    first_name: str
    last_name: str
