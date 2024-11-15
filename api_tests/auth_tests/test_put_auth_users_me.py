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
@allure.story("Изменение информации об авторизованном мною пользователе")
@allure.suite("/auth/users")
@allure.description("PUT /auth/users/me")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPutAuthUsersMe:
    fake = Faker()

    @pytest.mark.parametrize("user_email", [
        fake.email()
    ])
    @pytest.mark.parametrize("user_id", [
        fake.random_digit()
    ])
    @allure.title("Изменение информации об авторизованном мною пользователе корректное")
    def test_check_put_auth_users_me(self, auth_api_client, get_user1_auth_token, user_email, user_id):
        response = auth_api_client.put_auth_users_me(cookies = {
            "token": get_user1_auth_token,
            "email": user_email,
            "id": user_id
        })
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)

    @pytest.mark.parametrize("user_token", [
        None,
        fake.random_digit()
    ])
    @pytest.mark.parametrize("user_email", [
        None
    ])
    @pytest.mark.parametrize("user_id", [
        None
    ])
    @allure.title("Изменение информации об авторизованном мною пользователе некорректное")
    def test_check_get_auth_users_me(self, auth_api_client, user_token, user_email,user_id):
        response = auth_api_client.put_auth_users_me(cookies = {
            "token": user_token,
            "email": user_email,
            "id": user_id
        })
        assert response.status == HTTPStatus.UNAUTHORIZED
        logger.info(response.status)
        logger.info(response.data)