from http import HTTPStatus
import allure
import pytest

from api_tests.conftest import set_user1_mail, get_user1_auth_token
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Изменение пароля пользователя")
@allure.suite("auth/users/set_password")
@allure.description(
    "POST /auth/users/set_password"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsersSetPassword:
    fake = Faker()

    @allure.title("Изменение пароля пользователя c корректными данными")
    @pytest.mark.parametrize("user_pwd", [
        fake.password()
    ])
    def test_check_post_auth_users_set_password(self, auth_api_client, get_user1_auth_token, user_pwd, set_user_pwd):
        response = auth_api_client.post_auth_users_set_password(cookies={
            "token": get_user1_auth_token,
            "new_password": user_pwd,
            "current_password": set_user_pwd
        })
        assert response.status == HTTPStatus.OK
        assert 'new_password' in response.data
        assert 'current_password' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Сброс пароля пользователя с некорректными данными")
    @pytest.mark.parametrize("user_token, new_user_pwd, user_pwd", [
        (None, None, None),
        (fake.random_digit(), None, fake.password()),
        (get_user1_auth_token, fake.password(), None),
        (get_user1_auth_token, fake.password(), fake.password())
    ])

    def test_check_post_auth_users_set_password(self, auth_api_client, user_token, new_user_pwd, user_pwd):
        response = auth_api_client.post_auth_users_set_password(cookies={
        "token": user_token,
        "new_password": new_user_pwd,
        "current_password": user_pwd
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)