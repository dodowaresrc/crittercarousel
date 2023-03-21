import abc
from typing import List

from fastapi import status

from crittercarousel.api.misc import FormattedJSONResponse
from crittercarousel.api.interfaces import CritterRouterInterface


class BaseService(metaclass=abc.ABCMeta):

    def __init__(
        self,
        router:CritterRouterInterface,
        path:str,
        methods:List[str],
        status_code:int=status.HTTP_200_OK,
        **kwargs
    ):

        self.router = router

        self.name = str(self)

        router.add_api_route(
            path,
            self.handle_request,
            methods=methods,
            status_code=status_code,
            response_class=FormattedJSONResponse,
            **kwargs)

    @abc.abstractmethod
    def handle_request(self, *args, **kwargs):
       pass
