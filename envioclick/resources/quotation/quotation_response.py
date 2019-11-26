from dataclasses import dataclass
from typing import List
from envioclick.resources.package import Package
from envioclick.resources.insurance import Insurance
from envioclick.resources.rate import Rate


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
