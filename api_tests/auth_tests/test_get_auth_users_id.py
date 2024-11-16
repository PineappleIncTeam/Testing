from http import HTTPStatus
from types import NoneType

import allure
import pytest
from pydantic_core.core_schema import NoneSchema

from api_tests.conftest import set_user1_mail, get_user1_auth_token, set_url
from base.logger import logger
from faker import Faker
from base.setup_manager import SetupManager


@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Получение информации о пользователе по id")
@allure.suite("/auth/users")
@allure.description("GET /auth/users/id")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestGetAuthUsersId:
    fake = Faker()

    @allure.title("Получение информации о пользователе по корректному id")
    def test_checking_get_auth_users_id(self, auth_api_client, get_user1_auth_token, test_check_get_auth_users_me):
        response = auth_api_client.get_auth_users_id(params = test_check_get_auth_users_me,
         cookies = {
        "token": get_user1_auth_token
         }
        )
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Получение информации о пользователе по корректному id с некорректным токеном")
    @pytest.mark.parametrize("user_token", [
        None,
        fake.random_digit()
    ])
    def test_checking_get_auth_users_id(self, auth_api_client, user_token, test_check_get_auth_users_me):
        response = auth_api_client.get_auth_users_id(params = test_check_get_auth_users_me,
         cookies = {
        "token": user_token
         }
        )
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)