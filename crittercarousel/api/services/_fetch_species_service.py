from crittercarousel.api.models import SpeciesModel
from crittercarousel.api.services._base_service import BaseService


class FetchSpeciesService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/species/{name}", ["GET"])

    def handle_request(self, name:str) -> SpeciesModel:

        with self.router.application.dbconnect() as context:

            return context.fetch_species(name)
