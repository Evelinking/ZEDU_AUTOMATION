import requests
import os
import pytest

BASE_URL = os.getenv("BASE_URL")

# --- POSITIVE TESTS (10) ---
def test_get_user_profile(auth_headers):
    response = requests.get(f"{BASE_URL}/users/me", headers=auth_headers)
    assert response.status_code == 200
    assert "email" in response.json()["data"]

def test_get_organizations(auth_headers):
    response = requests.get(f"{BASE_URL}/organizations", headers=auth_headers)
    assert response.status_code in [200, 201]

def test_get_channels(auth_headers):
    response = requests.get(f"{BASE_URL}/channels", headers=auth_headers)
    assert response.status_code in [200, 404] # 404 is okay if no channels exist

def test_check_notifications(auth_headers):
    response = requests.get(f"{BASE_URL}/notifications", headers=auth_headers)
    assert response.status_code in [200, 404]

def test_get_contacts(auth_headers):
    response = requests.get(f"{BASE_URL}/contacts", headers=auth_headers)
    assert response.status_code in [200, 404]

def test_get_settings(auth_headers):
    response = requests.get(f"{BASE_URL}/settings", headers=auth_headers)
    assert response.status_code in [200, 404]

def test_get_workspace_info(auth_headers):
    response = requests.get(f"{BASE_URL}/workspaces", headers=auth_headers)
    assert response.status_code in [200, 404]

def test_get_active_sessions(auth_headers):
    response = requests.get(f"{BASE_URL}/auth/sessions", headers=auth_headers)
    assert response.status_code == 200

def test_get_roles(auth_headers):
    response = requests.get(f"{BASE_URL}/roles", headers=auth_headers)
    assert response.status_code == 200

def test_verify_token_validity(auth_headers):
    response = requests.get(f"{BASE_URL}/auth/verify", headers=auth_headers)
    assert response.status_code == 200

# --- NEGATIVE TESTS (10) ---
def test_login_invalid_password():
    payload = {"email": "test@zedu.chat", "password": "wrongpassword"}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == 401
    assert "message" in response.json()

def test_access_without_token():
    response = requests.get(f"{BASE_URL}/users/me")
    assert response.status_code == 401

def test_get_invalid_user_id(auth_headers):
    response = requests.get(f"{BASE_URL}/users/invalid123", headers=auth_headers)
    assert response.status_code in [400, 404]

def test_invalid_email_format():
    payload = {"email": "bad-email", "password": "any"}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code in [400, 401, 422]

def test_empty_login_payload():
    response = requests.post(f"{BASE_URL}/auth/login", json={})
    assert response.status_code in [400, 401, 422]

def test_malformed_token_access():
    headers = {"Authorization": "Bearer not-a-real-token"}
    response = requests.get(f"{BASE_URL}/users/me", headers=headers)
    assert response.status_code == 401

def test_invalid_method_on_profile(auth_headers):
    response = requests.delete(f"{BASE_URL}/users/me", headers=auth_headers)
    assert response.status_code in [405, 401, 403]

def test_login_unregistered_user():
    payload = {"email": "nonexistent@zedu.chat", "password": "password"}
    response = requests.post(f"{BASE_URL}/auth/login", json=payload)
    assert response.status_code == 401

def test_access_protected_route_with_expired_token():
    headers = {"Authorization": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.expired"}
    response = requests.get(f"{BASE_URL}/notifications", headers=headers)
    assert response.status_code == 401

def test_invalid_content_type(auth_headers):
    response = requests.post(f"{BASE_URL}/organizations", data="not-json", headers=auth_headers)
    assert response.status_code in [400, 415]

# --- EDGE CASES (5) ---
def test_long_string_query(auth_headers):
    long_str = "A" * 500
    response = requests.get(f"{BASE_URL}/users?search={long_str}", headers=auth_headers)
    assert response.status_code in [200, 400, 414]

def test_special_char_id(auth_headers):
    response = requests.get(f"{BASE_URL}/organizations/!@#$", headers=auth_headers)
    assert response.status_code in [400, 404]

def test_numeric_email_login():
    response = requests.post(f"{BASE_URL}/auth/login", json={"email": 12345, "password": "p"})
    assert response.status_code in [400, 401, 422]

def test_empty_search_query(auth_headers):
    response = requests.get(f"{BASE_URL}/users?search=", headers=auth_headers)
    assert response.status_code == 200

def test_large_json_payload(auth_headers):
    big_data = {"name": "A" * 2000}
    response = requests.patch(f"{BASE_URL}/users/me", json=big_data, headers=auth_headers)
    assert response.status_code in [200, 400, 413]