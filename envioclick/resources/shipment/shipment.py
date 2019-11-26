import os
from typing import ClassVar

from envioclick.resources import Resource
from envioclick.resources import ShipmentRequest
from envioclick.resources import ShipmentResponse

SANDBOX = os.getenv('SANDBOX_MODE')


class Shipment(Resource):
    _endpoint: ClassVar[str] = '/sandbox_shipment/request' if SANDBOX else '/shipment/request'

    @classmethod
    def create(cls, shipment_request: ShipmentRequest) -> 'ShipmentResponse':
        response = cls._client.post(cls._endpoint, json=shipment_request.to_dict())
        return ShipmentResponse(**response)
