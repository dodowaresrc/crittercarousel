from typing import List

from crittercarousel.api.models import SpeciesModel
from crittercarousel.api.services._base_service import BaseService


class GetSpeciesService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/species", ["GET"])

    def handle_request(self, name:str=None) -> List[SpeciesModel]:

        with self.router.application.dbconnect() as context:

            species_generator = context.get_species(name=name)

            return [x for x in species_generator]
