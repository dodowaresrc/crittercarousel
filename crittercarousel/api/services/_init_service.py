from fastapi import Response, status

from crittercarousel.api.services._base_service import BaseService

class InitService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/init", ["POST"])

    def handle_request(self, drop:bool=False):

        with self.router.application.dbconnect() as context:
            context.init(drop=drop)

        return Response(status_code=status.HTTP_200_OK)
