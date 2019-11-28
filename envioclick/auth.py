import os
from typing import Optional

API_KEY = os.getenv('API_KEY')


def api_auth_str() -> Optional[str]:
    return API_KEY
