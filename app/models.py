from dataclasses import dataclass, field


@dataclass
class Actor:
    id: int = field(init=False)
    first_name: str
    last_name: str
