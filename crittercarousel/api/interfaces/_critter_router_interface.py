import abc
from ._critter_application_interface import CritterApplicationInterface

class CritterRouterInterface(metaclass=abc.ABCMeta):

    @abc.abstractproperty
    def application(self) -> CritterApplicationInterface:
        pass
