import pytest
import os
import sys
from dotenv import load_dotenv

# This line fixes the "No module named ZEDU_AUTOMATION" error
# It tells Python to look inside the current folder for your code
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(_file_), '.')))

from utils.auth import get_auth_token

load_dotenv()

@pytest.fixture(scope="session")
def auth_headers():
    """This fixture provides the Authorization header to all tests."""
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
