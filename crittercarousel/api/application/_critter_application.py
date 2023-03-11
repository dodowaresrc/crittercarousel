from contextlib import contextmanager
from typing import ContextManager

from fastapi import FastAPI

from crittercarousel.api.database import CritterContext, DatabaseClient
from crittercarousel.api.interfaces import CritterApplicationInterface

from ._critter_router import CritterRouter


class CritterApplication(FastAPI, CritterApplicationInterface):

    def __init__(self):

        super().__init__()

        self.include_router(CritterRouter(self))

        self._database_client = DatabaseClient()

    @contextmanager
    def dbconnect(self) -> ContextManager[CritterContext]:
        with self._database_client.connect() as context:
            yield context
