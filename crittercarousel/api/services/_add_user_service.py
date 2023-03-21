from fastapi import Response, status

from crittercarousel.api.models import UserModel

from ._base_service import BaseService
from crittercarousel.api.interfaces import CritterRouterInterface


class AddUserService(BaseService):

    def __init__(self, router:CritterRouterInterface) -> UserModel:

        super().__init__(router, "/users", ["POST"], status_code=status.HTTP_201_CREATED)

    def handle_request(self, name:str):

        user = UserModel(
            name=name,
            clams=100,
            spawn_count=0,
            adopt_count=0,
            glue_count=0)

        with self.router.application.dbconnect() as context:
            context.assert_no_user(name)
            context.insert_user(user)

        return user
