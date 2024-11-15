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
@allure.story("Удаление авторизованного мною пользователе")
@allure.suite("/auth/users/me")
@allure.description("DELETE /auth/users/me")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestDeleteAuthUsersMe:
    fake = Faker()

    @allure.title("Удаление авторизованного мною пользователя корректное")
    def test_check_delete_auth_users_me(self, auth_api_client, get_user1_auth_token):
        response = auth_api_client.delete_auth_users_me(cookies = {
            "token": get_user1_auth_token
        })
        assert response.status == HTTPStatus.OK
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Удаление авторизованного мною пользователя некорректное")

    @pytest.mark.parametrize("user_token", [
        None,
        fake.random_digit()
    ])
    def test_check_delete_auth_users_me(self, auth_api_client, user_token):
        response = auth_api_client.delete_auth_users_me(cookies = {
            "token": user_token
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)