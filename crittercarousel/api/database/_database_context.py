from contextlib import contextmanager
from typing import Any, Dict, Generator, List

class DatabaseContext:

    def __init__(self):

        self._cursor = None

    @contextmanager
    def start(self, connection):

        with connection.cursor() as cursor:
             with connection.transaction():
                  self._cursor = cursor
                  yield

    def execute(self, statement:str, values:List=None):

        if not self._cursor:
            raise RuntimeError("cursor not open")

        #print("statement: %s" % statement)
        #print("values:    %s" % values)

        return self._cursor.execute(statement, values)

    def select(
        self,
        table:str,
        columns:List[str]=None,
        where_eq:Dict[str, Any]=None,
        where_ne:Dict[str, Any]=None,
        where_gt:Dict[str, Any]=None,
        where_lt:Dict[str, Any]=None,
        where_le:Dict[str, Any]=None,
        where_ge:Dict[str, Any]=None,
        where_is_null:List[str]=None,
        where_not_null:List[str]=None,
        limit:int=None
    ) -> Generator[Dict, None, None]:

        phrases = [
            "select",
            ",".join(columns) if columns else "*",
            "from",
            table
        ]

        values = []
        wheres = []

        for (data, operator) in (
            (where_eq, "="), 
            (where_ne, "!="),
            (where_gt, ">"),
            (where_lt, "<"),
            (where_ge, ">="),
            (where_le, "<=")
        ):
            if data:
                for (key, value) in data.items():
                    if value is not None:
                        wheres.append(f"{key} {operator} %s")
                        values.append(value)

        if where_is_null:
            for key in where_is_null:
                wheres.append(f"{key} is null")

        if where_not_null:
            for key in where_not_null:
                wheres.append(f"{key} is not null")

        if wheres:
            phrases.append("where")
            phrases.append(" and ".join(wheres))

        if limit is not None:
            phrases.append("limit %s")
            values.append(limit)

        statement = " ".join(phrases)

        self.execute(statement, values)

        return self._cursor

    def insert(self, table:str, data:Dict, ignore:List=None) -> None:

        keys = sorted(data.keys())

        if ignore:
            keys = [x for x in keys if x not in ignore]
        
        phrases = [
            f"insert into {table} (",
            ",".join(keys),
            ") values (",
            ",".join([f"%({x})s" for x in keys]),
            ")"
        ]

        statement = "".join(phrases)

        self.execute(statement, data)

    def update(self, table:str, data:Dict, primary_keys:List) -> None:

        update_keys = [x for x in sorted(data.keys()) if x not in primary_keys]

        phrases = [
            f"update {table} set (",
            ",".join(update_keys),
            ") = (",
            ",".join([f"%({x})s" for x in update_keys]),
            ") where ",
            " and ".join([f"{x}=%({x})s" for x in primary_keys])
        ]

        statement = " ".join(phrases)

        self.execute(statement, data)

    def delete(self, table:str, where_eq:Dict) -> None:

        wheres = []
        values = []

        for key, value in where_eq.items():
            wheres.append(f"{key}=%s")
            values.append(value)

        phrases = [
            "delete from",
            table,
            "where",
            " and ".join(wheres)
        ]

        statement = " ".join(phrases)

        self.execute(statement, values)
