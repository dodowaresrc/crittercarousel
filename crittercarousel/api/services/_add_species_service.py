from fastapi import status, HTTPException

from crittercarousel.api.models import SpeciesModel

from ._base_service import BaseService
from crittercarousel.api.interfaces import CritterRouterInterface


class AddSpeciesService(BaseService):

    def __init__(self, router:CritterRouterInterface) -> SpeciesModel:

        super().__init__(router, "/species", ["POST"], status_code=status.HTTP_201_CREATED)

    def handle_request(self, name:str):

        species = SpeciesModel(name=name)
            
        with self.router.application.dbconnect() as context:
            context.assert_no_species(name)
            context.insert_species(species)

        return species
