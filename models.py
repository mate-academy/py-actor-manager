from dataclasses import dataclass
from typing import Optional

@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str