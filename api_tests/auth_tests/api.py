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

    def post_auth_logout(
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_logout'],
            json=params,
            schema=schema,
            **kwargs,
        )

    def get_auth_users(
            self,
            user_id: str = None,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.get(
            auth_api_routes['auth']['get_users'].format(user_id),
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users(
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users'],
            json=params,
            schema=schema,
            **kwargs,
        )

    def get_auth_users_id( #как правильно писать?
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.get(
            auth_api_routes['auth']['get_users_id'],
            json=params,
            schema=schema,
            **kwargs
        )

    def put_auth_users_id( #как правильно писать?
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.put(
            auth_api_routes['auth']['get_users_id'],
            json=params,
            schema=schema,
            **kwargs
        )

    def patch_auth_users_id( #как правильно писать?
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.patch(
            auth_api_routes['auth']['get_users_id'],
            json=params,
            schema=schema,
            **kwargs
        )

    def delete_auth_users_id( #как правильно писать?
            self,
            params: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.patch(
            auth_api_routes['auth']['delete_users_id'],
            json=params,
            schema=schema,
            **kwargs
        )

    def get_auth_users_me(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.get(
            auth_api_routes['auth']['get_users_me'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def put_auth_users_me(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.put(
            auth_api_routes['auth']['put_users_me'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def patch_auth_users_me(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.patch(
            auth_api_routes['auth']['patch_users_me'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def delete_auth_users_me(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.delete(
            auth_api_routes['auth']['delete_users_me'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_resend_activation(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_resend_activation'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_reset_email(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_reset_emai'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_reset_email_confirm(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_reset_email_confirm'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_reset_password(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_reset_password'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_set_email(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_set_email'],
            json=cookies,
            schema=schema,
            **kwargs
        )

    def post_auth_users_set_password(
            self,
            cookies: dict = None,
            schema: dict = None, **kwargs
    ) -> BaseResponseModel:
        return self.post(
            auth_api_routes['auth']['post_users_set_password'],
            json=cookies,
            schema=schema,
            **kwargs
        )