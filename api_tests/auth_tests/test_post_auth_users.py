from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Создание пользователя")
@allure.suite("auth/users")
@allure.description(
    "POST /auth/users"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsers:
    fake = Faker()

    @pytest.mark.parametrize("user_mail, user_pwd", [
        ('valid_email', 'valid_pass'),
        (fake.email(), fake.password()),
    ])

    @allure.title("Создание пользователя с корректным логином и паролем")
    def test_check_post_auth_users(self,
                                         auth_api_client,
                                         user_mail,
                                         user_pwd):
        response = auth_api_client.post_auth_users(params={
            "email": user_mail,
            "password": user_pwd,
            "re_password": user_pwd
        })
        assert response.status == HTTPStatus.OK
        assert 'email' in response.data
        assert 'id' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @pytest.mark.parametrize("user_mail, user_pwd", [
        (None, None),
        ('valid_email', None),
        (None, 'valid_pass'),
        (fake.email(), fake.password()),
    ])

    @allure.title("Создание пользователя с некорректным логином и паролем")
    def test_check_post_auth_users(self,
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

        response = auth_api_client.post_auth_users(params={
            "email": user_mail,
            "password": user_pwd,
            "re_password": user_pwd
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)