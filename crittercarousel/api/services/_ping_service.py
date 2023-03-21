from ._base_service import BaseService

class PingService(BaseService):

    def __init__(self, router):
        super().__init__(router, "/ping", ["GET"])

    def handle_request(self):
        return {"ping":"pong"}
