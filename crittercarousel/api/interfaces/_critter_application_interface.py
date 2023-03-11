from contextlib import contextmanager
import abc
from collections.abc import Generator

from crittercarousel.api.database import CritterContext

class CritterApplicationInterface(metaclass=abc.ABCMeta):

    @contextmanager
    @abc.abstractmethod
    def dbconnect(self) -> Generator[CritterContext, None, None]:
        pass
