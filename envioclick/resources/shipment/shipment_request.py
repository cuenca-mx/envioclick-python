from dataclasses import dataclass
from typing import List

from envioclick.resources.insurance import Insurance
from envioclick.resources.package import Package
from envioclick.resources.rate import Rate


@dataclass
class Data:
    packages: List[Package]
    insurance: Insurance
    origin_zip_code: int
    destination_zip_code: int
    rates: List[Rate]
    id_carriers_no_ws_result: int


@dataclass
class StatusMessage:
    request: str

    def to_dict(self):
        return dict(
            request=self.request
        )


@dataclass
class ShipmentRequest:
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data

    def to_dict(self):
        return dict(
            status=self.status,
            status_codes=self.status_codes,
            status_messages=[message.to_dict() for message in self.status_messages],
            data=self.data.to_dict()
        )
