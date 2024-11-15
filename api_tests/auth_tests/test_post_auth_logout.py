from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Удаление token пользователя")
@allure.suite("/auth/token/logout")
@allure.description(
    "POST /auth/token/logout, Вызывается после нажатия на кнопку Logout"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthLogout:
    fake = Faker()

    @allure.title("Удаление токена авторизованного пользователя")
    def test_check_post_auth_valid_logout(self, auth_api_client, get_user1_auth_token):
        response = auth_api_client.post_auth_logout(params={
            "Authorization": get_user1_auth_token
        })
        assert response.status == HTTPStatus.OK
        assert 'id' in response.data
        assert 'email' in response.data
        logger.info(response.status)
        logger.info(response.data)

    @allure.title("Удаление токена неавторизованного пользователя")
    def test_check_post_auth_valid_logout(self, auth_api_client, get_user1_auth_token):
        response = auth_api_client.post_auth_logout(params={
            "Authorization": get_user1_auth_token
        })
        assert response.status == HTTPStatus.UNAUTHORIZED
        logger.info(response.status)
        logger.info(response.data)




