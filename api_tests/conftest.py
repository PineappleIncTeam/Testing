import pytest
import requests
from api_tests.auth_tests.routs import auth_api_routes
from base.logger import logger
from base.setup_manager import SetupManager


@pytest.fixture(scope="session")
def setup_manager():
    return SetupManager()

@pytest.fixture(scope="session")
def set_url(setup_manager):
    return setup_manager.set_url()

@pytest.fixture(scope="session")
def set_user1_mail(setup_manager):
    return setup_manager.get_user_mail1()

@pytest.fixture(scope="session")
def set_user_pwd(setup_manager):
    return setup_manager.get_user_pwd()

@pytest.fixture(scope="session")
def get_user1_auth_token(set_url, set_user1_mail, set_user_pwd):
    response = requests.post(
        url=f'{set_url}{auth_api_routes["auth"]["post_login"]}',
        json={
            "email": set_user1_mail,
            "password": set_user_pwd,
        }
    )
    try:
        return response.json()['auth_token']
    except KeyError:
        logger.error("auth_token not found in response")
        return None

@pytest.fixture
def test_check_get_auth_users_me(set_url, get_user1_auth_token):
    response = requests.get(
        url = f'{set_url}{auth_api_routes["auth"]["get_users_me"]}',
        json = {"token": get_user1_auth_token}
    )
    try:
        return response.json()['id']
    except KeyError:
        logger.error("id not found in response")
        return None