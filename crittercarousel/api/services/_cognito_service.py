import jwt
from fastapi import HTTPException, Request, status
from fastapi.security import HTTPBearer
from jwt import PyJWKClient

from crittercarousel.api.misc import getenv
from crittercarousel.api.services._base_service import BaseService


class CognitoHelper:

    def __init__(self):

        self.region = getenv("COGNITO_REGION")

        self.pool_id = getenv("COGNITO_POOL_ID")

        base_url = f"https://cognito-idp.{self.region}.amazonaws.com"

        jwk_url = f"{base_url}/{self.pool_id}/.well-known/jwks.json"

        self.jwk_client = PyJWKClient(jwk_url)

    async def authenticate(self, request):

        try:

            http_bearer = HTTPBearer()

            jwt_token = await http_bearer(request)

            jwt_bytes = jwt_token.credentials.encode(encoding="UTF-8")

            jwk_key = self.jwk_client.get_signing_key_from_jwt(jwt_bytes)

            jwt.decode(jwt_bytes, jwk_key.key, algorithms=["RS256"])

        except:

            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)

class CognitoService(BaseService):

    def __init__(self, router):

        super().__init__(router, "/hello", ["GET"])

        self.cognito_helper = CognitoHelper()
    
    async def handle_request(self, request:Request):

        await self.cognito_helper.authenticate(request)

        return "OK"
