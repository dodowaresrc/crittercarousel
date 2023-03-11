from crittercarousel.api.services._base_service import BaseService
from crittercarousel.api.models import UserModel
from typing import List

class GetUsersService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/users", ["GET"])

    def handle_request(self, name:str=None, limit:int=None) -> List[UserModel]:
        
        with self.router.application.dbconnect() as context:

            user_generator = context.get_users(name=name, limit=limit)

            return [x for x in user_generator]
