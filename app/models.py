from dataclasses import dataclass as dc


@dc
class Actor:
    id: int
    first_name: str
    last_name: str
