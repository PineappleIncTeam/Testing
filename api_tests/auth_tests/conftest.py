import pytest
from api_tests.auth_tests.api import AuthApiClient

@pytest.fixture
def auth_api_client(set_url):
    return AuthApiClient(base_url=set_url)