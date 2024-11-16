from http import HTTPStatus
import allure
import pytest

from api_tests.conftest import set_user1_mail
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Сброс пароля пользователя")
@allure.suite("auth/users/reset_password")
@allure.description(
    "POST /auth/users/reset_password"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsersResetPassword:
    fake = Faker()


    @allure.title("Изменение пароля пользователя c корректными данными")
    def test_check_post_auth_users_reset_password(self, auth_api_client, get_user1_auth_token, set_user1_mail):
        response = auth_api_client.post_auth_users_reset_password(cookies={
            "token": get_user1_auth_token,
            "email": set_user1_mail
        })
        assert response.status == HTTPStatus.OK
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Сброс пароля пользователя с некорректными данными")
    @pytest.mark.parametrize("user_token, user_mail", [
        (None, None),
        ('valid_token', None),
        (None, 'valid_mail'),
        (fake.random_digit(), fake.random_digit())
    ])

    def test_check_post_auth_users_reset_password(self, auth_api_client, user_token, user_mail):
        response = auth_api_client.post_auth_users_reset_password(cookies={
        "token": user_token,
        "email": user_mail
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)