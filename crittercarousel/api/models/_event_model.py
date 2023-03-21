from datetime import datetime
from typing import List, Optional, Tuple

from pydantic import BaseModel

class EventModel(BaseModel):
    username: str
    species: str
    name: str
    action: str
    time: datetime
    id: Optional[int]=None

    @classmethod
    def get_insert_statement(cls, event):

        statement = " ".join([
            "insert into events",
            "(name, species, action, time)",
            "values('%s', '%s', '%s', '%s')",
        ])

        values = (event.name, event.species, event.action, cls.to_timestamp(event.time))

        return (statement, values)

    @classmethod
    def get_select_statement(
        cls,
        name:str=None,
        species:str=None,
        action:str=None,
        time_lt:datetime=None,
        time_gt:datetime=None,
        limit:int=None
    ) -> Tuple[str, List[str]]:

        phrases = ["select * from events"]
        wheres = []
        values = []

        if name is not None:
            wheres.append("name = '%s'")
            values.append(name)

        if species is not None:
            wheres.append("species = '%s'")
            values.append(species)

        if action is not None:
            wheres.append("action = '%s'")
            values.append(action)

        if time_lt is not None:
            wheres.append("time < '%s'")
            values.append(cls.to_timestamp(time_lt))
                             
        if time_gt is not None:
            wheres.append("time > '%s'")
            values.append(cls.to_timestamp(time_gt))

        if wheres:
            phrases.append("where")
            phrases.append(" and ".join(wheres))

        if limit is not None:
            phrases.append("limit %s")
            values.append(limit)

        statement = " ".join(phrases)

        return (statement, values)

    @classmethod
    def get_update_statement(cls):
        raise RuntimeError("events cannot be updated")
