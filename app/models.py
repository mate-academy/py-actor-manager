from dataclasses import dataclass
import sqlite3


@dataclass
class Actor:
    id: int
    first_name: str
    last_name: str
    
    
