from http import HTTPStatus
import allure
import pytest
from base.logger import logger
from faker import Faker

@allure.feature("API.Auth API")
@allure.epic("API.Auth API")
@allure.story("Изменение эл.почты пользователя")
@allure.suite("auth/users/reset_email_confirm")
@allure.description(
    "POST /auth/users/reset_email_confirm"
)
@allure.label("severity", "High")
@allure.label("automationTool", "Pytest")
@allure.label("layer", "api")
@allure.label("priority", "Высокий")
@allure.label("owner", "PolinaPronina07")

class TestPostAuthUsersResetEmailConfirm:
    fake = Faker()


    @allure.title("Изменение эл.почты пользователя c корректными данными")
    @pytest.mark.parametrize("user_mail", [
       fake.email()
    ])
    def test_check_post_auth_users_reset_email_confirm(self, auth_api_client, get_user1_auth_token, user_mail):
        response = auth_api_client.post_auth_users_reset_email_confirm(cookies={
            "token": get_user1_auth_token,
            "new_email": user_mail
        })
        assert response.status == HTTPStatus.OK
        assert 'new_email' in response.data
        logger.info(response.status)
        logger.info(response.data)


    @allure.title("Сброс эл.почты пользователя с некорректными данными")
    @pytest.mark.parametrize("user_token, user_mail", [
        (None, None),
        ('valid_token', None),
        (None, 'valid_mail'),
        (fake.random_digit(), fake.english_word())
    ])

    def test_check_post_auth_users_reset_email_confirm(self, auth_api_client, user_token, user_mail):
        response = auth_api_client.post_auth_users_reset_email_confirm(cookies={
        "token": user_token,
        "new_email": user_mail
        })
        assert response.status == HTTPStatus.BAD_REQUEST
        logger.info(response.status)
        logger.info(response.data)