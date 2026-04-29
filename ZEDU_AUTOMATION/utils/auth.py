import requests
import os
from dotenv import load_dotenv

# This tells the code to look at your .env file
load_dotenv()

def get_auth_token():
    url = f"{os.getenv('BASE_URL')}/auth/login"
    payload = {
        "email": os.getenv("TEST_USER_EMAIL"),
        "password": os.getenv("TEST_USER_PASSWORD")
    }
    # We send the login request to Zedu
    response = requests.post(url, json=payload)
    
    # We grab the token from the response
    if response.status_code == 200:
        return response.json().get("data").get("token")
    else:
        print("Login failed! Check your .env credentials.")
        return None