from datetime import datetime
from fastapi import HTTPException, status

from crittercarousel.api.models import EventModel, StatusModel 
from crittercarousel.api.services._base_service import BaseService


class PostEventService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/events", ["POST"])

    def handle_request(self, username:str, species:str, name:str, action:str) -> dict:

        now = datetime.now()

        event = EventModel(username=username, species=species, name=name, action=action, time=now)

        message = None

        with self.router.application.dbconnect() as context:

            user = context.fetch_user(username)

            critter = context.fetch_critter(username, species, name)

            critter_status = StatusModel.from_critter(critter)

            if action in ("feed", "pet", "play", "adopt") and critter_status.status == "dead":
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"{critter.name} the {critter.species} is dead")
            
            if action == "feed":
                critter.last_feed_time = now
                context.update_critter(critter)
                message = f"{critter.name} the {critter.species} is not hungry"

            elif action == "pet":
                critter.last_pet_time = now
                context.update_critter(critter)
                message = f"{critter.name} the {critter.species} is not sad"

            elif action == "play":
                critter.last_play_time = now
                context.update_critter(critter)
                message = f"{critter.name} the {critter.species} is not bored"

            elif action == "adopt":
                if critter_status.status != "happy":
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"{critter.name} the {critter.species} is not happy")
                user.clams += 35
                user.adopt_count += 1
                context.update_user(user)
                context.delete_critter(critter)
                message = f"{critter.name} the {critter.species} has been adopted (you get 35 clams)"

            elif action == "glue":
                if critter_status.status != "dead":
                    raise HTTPException(
                        status_code=status.HTTP_400_BAD_REQUEST,
                        detail=f"{critter.name} the {critter.species} is still alive")
                user.clams += 2
                user.glue_count += 1
                context.update_user(user)
                context.delete_critter(critter)
                message = f"the glue factory gives you 2 clams for the corpse of {critter.name} the {critter.species}"

            else:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail=f"unknown action: {action}")
            
            context.insert_event(event)

        return {"message": message}
