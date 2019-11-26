from dataclasses import dataclass
from typing import Optional, List
from envioclick.resources.package import Package


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


@dataclass
class Data:
    package: Package
    origin: Destination
    destination: Destination
    guide: str
    url: str
    tracker: str
    id_order: int


@dataclass
class StatusMessage:
    request: str


@dataclass
class ShipmentResponse:
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data
