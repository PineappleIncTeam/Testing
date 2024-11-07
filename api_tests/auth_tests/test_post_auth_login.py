from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Получение token пользователя")
@allure.suite("/auth/token/login")
@allure.description(
    "POST /auth/token/login, Вызывается после нажатия на кнопку Login"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "eeefimov")
class TestPostAuthLogin:
    fake = Faker()

    @allure.title("Получение токена, зарегистрированного пользователя")
    def test_check_post_auth_valid_login(self,
                                         auth_api_client,
                                         set_user1_mail,
                                         set_user_pwd):
        response = auth_api_client.post_auth_login(params={
            "email": set_user1_mail,
            "password": set_user_pwd,
        })
        assert response.status == HTTPStatus.OK
        assert 'auth_token' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @pytest.mark.parametrize("user_mail, user_pwd", [
        (None, None),
        ('valid_email', None),
        (None, 'valid_pass'),
        (fake.email(), fake.password()),
    ])
    @allure.title("Получение токена, невалидные креды пользователя")
    def test_check_post_auth_invalid_login(self,
                                           auth_api_client,
                                           set_user1_mail,
                                           set_user_pwd,
                                           user_mail,
                                           user_pwd
                                           ):
        if user_mail == 'valid_email':
            user_mail = set_user1_mail
        if user_pwd == 'valid_pass':
            user_mail = set_user_pwd

        response = auth_api_client.post_auth_login(params={
            "email": user_mail,
            "password": user_pwd,
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)