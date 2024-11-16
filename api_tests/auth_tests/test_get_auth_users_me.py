from http import HTTPStatus
from types import NoneType

import allure
import pytest
from pydantic_core.core_schema import NoneSchema
from requests import session

from api_tests.conftest import set_user1_mail, get_user1_auth_token
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Получение информации об авторизованном мною пользователе")
@allure.suite("/auth/users")
@allure.description("GET /auth/users/me")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestGetAuthUsersMe:
    fake = Faker()

    @allure.title("Получение информации об авторизованном мною пользователе корректное")
    def test_checking_get_auth_users_me(self, auth_api_client, get_user1_auth_token):
        response = auth_api_client.get_auth_users_me(cookies = {"token": get_user1_auth_token})
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)

    @pytest.mark.parametrize("user_token", [
        None,
        fake.random_digit()
    ])
    @allure.title("Получение информации об авторизованном мною пользователе некорректное")
    def test_check_get_auth_users_me(self, auth_api_client, get_user1_auth_token, user_token):
        response = auth_api_client.get_auth_users_me(cookies = {"token": user_token})
        assert response.status == HTTPStatus.UNAUTHORIZED
        logger.info(response.status)
        logger.info(response.data)