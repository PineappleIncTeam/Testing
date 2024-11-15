from http import HTTPStatus
from types import NoneType

import allure
import pytest
from pydantic_core.core_schema import NoneSchema

from api_tests.conftest import set_user1_mail, get_user1_auth_token
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Получение списка авторизованных пользователей")
@allure.suite("/auth/users")
@allure.description("GET /auth/users")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestGetAuthUsers:
    fake = Faker()

    @allure.title("Получение корректное списка авторизованных пользователей")
    def test_check_get_auth_users(self, auth_api_client, get_user1_auth_token):
        response = auth_api_client.get_auth_users(cookies = {"token": get_user1_auth_token})
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)

    @pytest.mark.parametrize("user_token", [
        None,
        fake.token()
    ])
    @allure.title("Получение некорректное списка авторизованных пользователей")
    def test_check_get_auth_users_invalid(self, auth_api_client, get_user1_auth_token, user_token):
        response = auth_api_client.get_auth_users(cookies = {"token": user_token})
        assert response.status == HTTPStatus.UNAUTHORIZED
        logger.info(response.status)
        logger.info(response.data)