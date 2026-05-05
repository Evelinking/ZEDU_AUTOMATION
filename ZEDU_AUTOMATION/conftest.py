import pytest
import os
import sys
from dotenv import load_dotenv

# This points the robot to the right folder
sys.path.append(os.path.dirname(os.path.abspath(_file_)))

from utils.auth import get_auth_token

load_dotenv()

@pytest.fixture(scope="session")
def auth_headers():
    token = get_auth_token()
    return {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
