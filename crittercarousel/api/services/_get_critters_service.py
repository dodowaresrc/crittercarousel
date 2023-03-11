from typing import List

from crittercarousel.api.models import CritterModel
from crittercarousel.api.services._base_service import BaseService

class GetCrittersService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/critters", ["GET"])

    def handle_request(self, username:str=None, species:str=None, name:str=None, limit:int=None) -> List[CritterModel]:

        with self.router.application.dbconnect() as context:

            critter_generator = context.get_critters(username=username, species=species, name=name, limit=limit)

            return [x for x in critter_generator]
