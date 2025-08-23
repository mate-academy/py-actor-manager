from dataclasses import dataclass


@dataclass
class Actor:
    """Dataclass representing an actor."""
    id: int
    first_name: str
    last_name: str
