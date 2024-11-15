from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Повторная отправка письма активации на эл.почту пользователя")
@allure.suite("auth/users/resend_activation")
@allure.description(
    "POST /auth/users/resend_activation"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsersResendActivation:
    fake = Faker()


    @allure.title("Повторная отправка письма активации на эл.почту пользователя c корректными данными")
    def test_check_post_auth_users_resend_activation(self, auth_api_client, get_user1_auth_token, set_user1_mail):
        response = auth_api_client.post_auth_users_resend_activation(cookies={
            "token": get_user1_auth_token,
            "email": set_user1_mail
        })
        assert response.status == HTTPStatus.OK
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)

    @allure.title("Повторная отправка письма активации на эл.почту пользователя с некорректными данными")
    @pytest.mark.parametrize("user_token, user_mail", [
        (None, None),
        ('valid_token', None),
        (None, 'valid_mail'),
        (fake.random_digit(), fake.email())
    ])

    def test_check_post_auth_users_resend_activation(self, auth_api_client, user_token, user_mail):
        response = auth_api_client.post_auth_users_resend_activation(cookies={
        "token": user_token,
        "email": user_mail
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)