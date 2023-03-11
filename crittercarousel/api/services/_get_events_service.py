from typing import List

from crittercarousel.api.models import EventModel
from crittercarousel.api.services._base_service import BaseService

class GetEventsService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/events", ["GET"])

    def handle_request(self, username:str=None, species:str=None, name:str=None, action:str=None) -> List[EventModel]:

        with self.router.application.dbconnect() as context:

            event_generator = context.get_events(username=username, species=species, name=name, action=action)

            return [x for x in event_generator]
