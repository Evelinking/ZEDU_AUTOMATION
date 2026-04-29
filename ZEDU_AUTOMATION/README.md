# Zedu API Automation Project
This is a Python-based API automation suite for the Zedu platform.

## Prerequisites
- Python 3.10+
- Pip

## Setup
1. Clone the repository.
2. Create a .env file in the root directory.
3. Add BASE_URL, EMAIL, and PASSWORD to the .env file.
4. Install dependencies: pip install -r requirements.txt

## Execution
Run the full suite using: pytest

## 📁 Project Overview
- *tests/test_profile.py*: Contains 25 automated test cases (10 Positive, 10 Negative, 5 Edge cases) covering user profile and authentication endpoints.
- *utils/auth.py*: Shared utility for programmatic authentication and token retrieval.
- *conftest.py*: Pytest configuration file containing the auth_headers fixture.
- *.env*: Local environment file for sensitive credentials (not tracked by Git).