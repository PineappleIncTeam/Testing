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
@allure.story("Изменение информации о пользователе по id")
@allure.suite("/auth/users")
@allure.description("PUT /auth/users/id")
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPutAuthUsersId:
    fake = Faker()

    @allure.title("Изменение информации о пользователе по id на корректные значения")
    @pytest.mark.parametrize("user_id, user_mail", [
        fake.random_int(1, 22, 1), fake.email()
    ])
    def test_check_put_auth_users_id(self, auth_api_client, user_id, user_mail, get_user1_auth_token):
        response = auth_api_client.put_auth_users_id(params = {
        "id": user_id,
        "email": user_mail
        },
         cookies = {
        "token": get_user1_auth_token
         }
        )
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)




    @allure.title("Изменение информации о пользователе по id на некорректные значения")
    @pytest.mark.parametrize("user_id, user_mail", [
        (fake.random_digit(), None),
        (None, fake.email())
    ])
    def test_check_put_auth_users_id(self, auth_api_client, user_id, user_mail, get_user1_auth_token):
        response = auth_api_client.put_auth_users_id(params={
            "id": user_id,
            "email": user_mail
        },
            cookies={
                "token": get_user1_auth_token
            }
        )
        assert response.status == HTTPStatus.BAD_REQUEST
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)