import os
from dataclasses import dataclass
from typing import ClassVar, List, Optional

from envioclick.resources import Resource
from envioclick.resources.package import Package
from envioclick.resources.status_message import StatusMessage

from .shipment_request import ShipmentRequest

SANDBOX = os.getenv('SANDBOX', 'false').lower() == 'true'


@dataclass
class Destination:
    company: str
    first_name: str
    last_name: str
    email: str
    phone: str
    street: str
    number: int
    suburb: str
    cross_street: str
    reference: str
    zip_code: int
    full_name: Optional[str] = None
    full_address: Optional[str] = None
    state: Optional[str] = None

    def to_dict(self):
        return dict(
            company=self.company,
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
            phone=self.phone,
            street=self.street,
            number=self.number,
            suburb=self.suburb,
            cross_street=self.cross_street,
            reference=self.reference,
            zip_code=self.zip_code,
            full_name=self.full_name,
            full_address=self.full_address,
            state=self.state,
        )


@dataclass
class Data:
    package: Package
    origin: Destination
    destination: Destination
    guide: str
    url: str
    tracker: str
    id_order: int

    def to_dict(self):
        return dict(
            package=self.package.to_dict(),
            origin=self.origin.to_dict(),
            destination=self.destination.to_dict(),
            guide=self.guide,
            url=self.url,
            tracker=self.tracker,
            id_order=self.id_order,
        )


@dataclass
class Shipment(Resource):
    _endpoint: ClassVar[
        str
    ] = '/sandbox_shipment/request' if SANDBOX else '/shipment/request'
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data

    @classmethod
    def create(cls, shipment_request: ShipmentRequest) -> 'Shipment':
        response = cls._client.post(
            cls._endpoint, json=shipment_request.to_dict()
        )
        return cls(**response)

    def to_dict(self):
        return dict(
            status=self.status,
            status_codes=self.status_codes,
            status_messages=[
                message.to_dict() for message in self.status_messages
            ],
            data=self.data.to_dict(),
        )
