from __future__ import annotations

import re
import sqlite3
from typing import Any

from app.models import Actor


class TableNameValidator:
    def __init__(self) -> None:
        self.pattern = re.compile(
            r"^[A-Za-z_][A-Za-z0-9_]*$"
        )

    def __set_name__(
            self,
            owner: type[Any],
            name: str
    ) -> None:
        self.private_name = "_" + name

    def __get__(
            self,
            instance: Any,
            owner: type[Any]
    ) -> str | None:
        return getattr(
            instance,
            self.private_name,
            None
        )

    def __set__(
            self,
            instance: Any,
            value: str
    ) -> None:
        if (
                instance is not None
                and not self.pattern.fullmatch(value)
        ):
            raise ValueError(
                f"Invalid table name {value}: bad format"
            )
        setattr(instance, self.private_name, value)


class ActorManager:
    table_name = TableNameValidator()

    def __init__(
            self,
            db_name: str,
            table_name: str
    ) -> None:
        self.db_name = db_name
        self.table_name = table_name
        self._conn = sqlite3.connect(db_name)
        self._conn.row_factory = sqlite3.Row
        self.cursor = self._conn.cursor()

    def close(self) -> None:
        self.cursor.close()
        self._conn.close()

    def create(
            self, first_name: str,
            last_name: str
    ) -> int:
        self.cursor.execute(
            f"INSERT INTO {self.table_name} "
            "(first_name, last_name) VALUES (?, ?)",
            (first_name, last_name)
        )
        self._conn.commit()
        return self.cursor.lastrowid

    def all(self) -> list[Actor]:
        list_of_actors_row_obj = self.cursor.execute(
            f"SELECT * FROM {self.table_name}"
        ).fetchall()
        return [
            Actor(
                id=actor_tuple["id"],
                first_name=actor_tuple["first_name"],
                last_name=actor_tuple["last_name"],
            )
            for actor_tuple
            in list_of_actors_row_obj
        ]

    def update(
            self,
            pk: int,
            new_first_name: str,
            new_last_name: str) -> int:
        self.cursor.execute(
            f"UPDATE {self.table_name} "
            "SET first_name = ?, last_name = ? "
            "WHERE id = ?",
            (new_first_name, new_last_name, pk)
        )
        self._conn.commit()
        return self.cursor.rowcount

    def delete(self, pk: int) -> int:
        self.cursor.execute(
            f"DELETE FROM {self.table_name} "
            "WHERE id = ?",
            (pk,)
        )
        self._conn.commit()
        return self.cursor.rowcount
