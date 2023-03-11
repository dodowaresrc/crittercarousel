from datetime import datetime

from fastapi import HTTPException, status

from crittercarousel.api.models import CritterModel
from crittercarousel.api.interfaces import CritterRouterInterface
from crittercarousel.api.services._base_service import BaseService

from ._base_service import BaseService


class SpawnCritterService(BaseService):

    def __init__(self, router:CritterRouterInterface):

        super().__init__(router, "/critters", ["POST"], status_code=status.HTTP_201_CREATED)

    def handle_request(self, username:str, species:str, name:str) -> CritterModel:

        now = datetime.now()

        with self.router.application.dbconnect() as context:

            context.assert_no_critter(username, species, name)

            context.fetch_species(species)

            user = context.fetch_user(username)

            if user.clams < 20:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="not enough clams to spawn a new critter"
                )
        
            critter = CritterModel(
                username=username,
                name=name,
                species=species,
                spawn_time=now,
                last_feed_time=now,
                last_pet_time=now,
                last_play_time=now
            )

            user.spawn_count += 1
            user.clams -= 20

            context.insert_critter(critter)
            context.update_user(user)

        return critter
