import pytest
import os
from dotenv import load_dotenv
# We import from the inner folder where the code actually lives
from ZEDU_AUTOMATION.utils.auth import get_auth_token

# This loads the hidden GitHub Secrets
load_dotenv()

@pytest.fixture(scope="session")
def auth_headers():
    """This fixture provides the Authorization header to all tests."""
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
