import pytest
from utils.auth import get_auth_token

@pytest.fixture(scope="session")
def auth_headers():
    """This fixture provides the Authorization header to all tests."""
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }