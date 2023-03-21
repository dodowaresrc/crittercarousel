
from contextlib import contextmanager
from typing import Generator

import psycopg
from psycopg.rows import dict_row

from crittercarousel.api.database._critter_context import CritterContext
from crittercarousel.api.misc import getenv


class DatabaseClient:

    def __init__(self):

        self._connstr = "postgresql://{0}:{1}@{2}:{3}/{4}".format(
            getenv("RDS_USERNAME", required=True),
            getenv("RDS_PASSWORD", required=True),
            getenv("RDS_HOSTNAME", required=True),
            getenv("RDS_PORT", required=True),
            getenv("RDS_DB_NAME", required=True)
        )

    @contextmanager
    def connect(self) -> Generator[CritterContext, None, None]:

        with psycopg.connect(self._connstr, row_factory=dict_row) as connection:
            context = CritterContext()
            with context.start(connection):
                yield context
