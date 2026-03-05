from dataclasses import dataclass


@dataclass
class Actor:
    id: int  # noqa: VNE003
    first_name: str
    last_name: str
