from base.api import BaseClient, BaseResponseModel
from api_tests.auth_tests.routs import auth_api_routes


class AuthApiClient(BaseClient):

    def post_auth_login(
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_login'],
            json=params,
            schema=schema,
            **kwargs,
        )