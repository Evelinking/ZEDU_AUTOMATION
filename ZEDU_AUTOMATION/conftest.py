import pytest
import os
import sys
from dotenv import load_dotenv

# This line fixes the folder path so the robot can find 'utils'
# Note the DOUBLE underscores in _file_
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
