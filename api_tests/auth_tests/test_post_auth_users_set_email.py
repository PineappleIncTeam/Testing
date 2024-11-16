from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Изменение эл.почты пользователя")
@allure.suite("auth/users/set_email")
@allure.description(
    "POST /auth/users/set_email"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsersSetEmail:
    fake = Faker()


    @allure.title("Изменение эл.почты пользователя c корректными данными")
    @pytest.mark.parametrize("user_mail", [
          fake.email()
    ])
    def test_check_post_auth_users_set_email(self, auth_api_client, get_user1_auth_token, set_user_pwd, user_mail):
        response = auth_api_client.post_auth_users_set_email(cookies={
            "token": get_user1_auth_token,
            "current_password": set_user_pwd,
            "new_email": user_mail
        })
        assert response.status == HTTPStatus.OK
        assert "current_password" in response.data
        assert 'new_email' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Сброс эл.почты пользователя с некорректными данными")
    @pytest.mark.parametrize("user_token, user_mail, user_pwd", [
        (None, None, None),
        ('valid_token', None, None),
        (None, 'valid_mail', None),
        (None, None, fake.password()),
        (fake.random_digit(), fake.email(), fake.password())
    ])

    def test_check_post_auth_users_set_email(self, auth_api_client, user_token, user_pwd, user_mail):
        response = auth_api_client.post_auth_users_set_email(cookies={
        "token": user_token,
        "current_password": user_pwd,
        "new_email": user_mail
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)