import sqlite3
from dataclasses import dataclass


@dataclass
class Actor:
    first_name: str
    last_name: str
