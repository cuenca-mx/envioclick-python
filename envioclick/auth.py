import os

API_KEY = os.getenv('API_KEY')


def api_auth_str() -> str:
    return f'Authorization {API_KEY}'
