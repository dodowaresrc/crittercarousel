from crittercarousel.api.models import CritterModel
from crittercarousel.api.services._base_service import BaseService


class FetchCritterService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/critters/{username}/{species}/{name}", ["GET"])

    def handle_request(self, username:str, species:str, name:str) -> CritterModel:

        with self.router.application.dbconnect() as context:

            return context.fetch_critter(username, species, name)
