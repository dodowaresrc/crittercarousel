from fastapi import APIRouter
import crittercarousel.api.services as services
from crittercarousel.api.interfaces import CritterApplicationInterface, CritterRouterInterface

class CritterRouter(APIRouter, CritterRouterInterface):

    def __init__(self, application):

        super().__init__(prefix="/api/v1")

        self._application = application

        for service_class in services.ALL_SERVICES:
            service_class(self)

    @property
    def application(self) -> CritterApplicationInterface:
        return self._application
