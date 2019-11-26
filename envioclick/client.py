import os
from typing import Any, ClassVar, Dict, Optional, Tuple, Union

from requests import Response, Session

from .resources import Quotation, Resource, Shipment, Tracking
from .version import __version__ as client_version

API_URL = 'https://api.envioclickpro.com/api/v1'


class Client:
    base_url: ClassVar[str] = API_URL
    headers: Dict[str, str]
    session: Session

    # resources
    quotation: ClassVar = Quotation
    shipment: ClassVar = Shipment
    tracking: ClassVar = Tracking

    def __init__(
            self, api_key: Optional[str] = None
    ):
        self.session = Session()
        self.headers = {
            'Authorization': api_key or os.getenv('API_KEY'),
            'User-Agent': f'envioclick/{client_version}'
        }
        Resource._client = self

    def get(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        return self.request('get', endpoint, **kwargs)

    def post(self, endpoint: str, **kwargs: Any) -> Dict[str, Any]:
        return self.request('post', endpoint, **kwargs)

    def request(
            self,
            method: str,
            endpoint: str,
            **kwargs: Any,
    ) -> Dict[str, Any]:
        url = self.base_url + endpoint
        headers = self.headers
        response = self.session.request(method, url, headers=headers, **kwargs)
        self._check_response(response)
        return response.json()

    @staticmethod
    def _check_response(response: Response) -> None:
        if response.ok:
            return
        response.raise_for_status()
