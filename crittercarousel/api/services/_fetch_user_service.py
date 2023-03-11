from crittercarousel.api.models import UserModel
from crittercarousel.api.services._base_service import BaseService


class FetchUserService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/users/{name}", ["GET"])

    def handle_request(self, name:str) -> UserModel:

        with self.router.application.dbconnect() as context:

            return context.fetch_user(name)
