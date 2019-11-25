from dataclasses import dataclass
from typing import List


@dataclass
class Insurance:
    content_value: float
    amount_insurance: float


@dataclass
class Package:
    content_value: float
    weight: float
    length: float
    height: float


@dataclass
class Rate:
    id_rates: int
    id_product: int
    product: str
    vehicle: str
    id_carrier: int
    carrier: str
    total: float
    delivery_type: str
    delivery_days: int


@dataclass
class Data:
    package: Package
    insurance: Insurance
    origin_zip_code: int
    destination_zip_code: int
    rates: List[Rate]
    id_carriers_no_ws_result: int


@dataclass
class StatusMessage:
    request: str


@dataclass
class QuotationResponse:
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data
