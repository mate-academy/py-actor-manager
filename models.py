from dataclasses import dataclass
from typing import Optional

@dataclass
class Actor:
    id: Optional[int]
    first_name: str
    last_name: str