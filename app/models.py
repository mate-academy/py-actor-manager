from dataclasses import dataclass


@dataclass
class Actor:
    """Representa um ator com identificador e nome completo."""
    id: int
    first_name: str
    last_name: str
