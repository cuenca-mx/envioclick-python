import os
from typing import Any, ClassVar, Dict, Optional, Tuple, Union
from requests import Response, Session
from .version import __version__ as client_version

from .resources import (
    Quotation,
    Resource,
    ShipmentRequest,
    ShipmentResponse,
    TrackingRequest,
    TrackingResponse
)

API_URL = 'https://api.envioclickpro.com/api/v1'


class Client:
    base_url: ClassVar[str] = API_URL
    headers: Dict[str, str]
    session: Session

    # resources
    quotation: ClassVar = Quotation
    shipment_request: ClassVar = ShipmentRequest
    shipment_response: ClassVar = ShipmentResponse
    tracking_request: ClassVar = TrackingRequest
    tracking_response: ClassVar = TrackingResponse

    def __init__(
            self, api_key: Optional[str] = None
    ):
        self.session = Session()
        self.headers = {
            'Authorization': api_key or os.getenv('API_KEY'),
            'User-Agent': f'mati-python/{client_version}'
        }
        Resource._client = self

    def get(self, **kwargs):
        pass

    def post(self, **kwargs):
        pass
