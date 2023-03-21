from crittercarousel.api.services._base_service import BaseService
from crittercarousel.api.models import StatusModel
from typing import List

class GetStatusService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/status", ["GET"])

    def handle_request(
        self,
        username:str=None,
        species:str=None,
        name:str=None,
        hungry:bool=None,
        sad:bool=None,
        bored:bool=None,
        happy:bool=None,
        dead:bool=None,
        health_lt:int=None,
        health_gt:int=None
    ) -> List[StatusModel]:
        
        status_list = []

        with self.router.application.dbconnect() as context:

            critter_generator = context.get_critters(username=username, species=species, name=name)

            for critter in critter_generator:

                status = StatusModel.from_critter(critter)

                if hungry is not None and (status.hunger > 0) != hungry:
                    continue

                if sad is not None and (status.sadness > 0) != sad:
                    continue

                if bored is not None and (status.boredom > 0) != bored:
                    continue

                if happy is not None and (status == "happy") != happy:
                    continue

                if dead is not None and (status.status == "dead") != dead:
                    continue

                if health_lt is not None and status.health >= health_lt:
                    continue

                if health_gt is not None and status.health <= health_gt:
                    continue

                status_list.append(status)

        return status_list
