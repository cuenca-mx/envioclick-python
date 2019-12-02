from dataclasses import dataclass
from typing import ClassVar, List

from envioclick.resources import Resource
from envioclick.resources.insurance import Insurance
from envioclick.resources.package import Package
from envioclick.resources.rate import Rate
from envioclick.resources.status_message import StatusMessage

from .quotation_request import QuotationRequest


@dataclass
class Data:
    package: Package
    insurance: Insurance
    origin_zip_code: str
    destination_zip_code: str
    rates: List[Rate]
    id_carriers_no_ws_result: str

    def to_dict(self):
        return dict(
            package=self.package.to_dict(),
            insurance=self.insurance.to_dict(),
            origin_zip_code=self.origin_zip_code,
            destination_zip_code=self.destination_zip_code,
            rates=[rate.to_dict() for rate in self.rates],
            id_carriers_no_ws_result=self.id_carriers_no_ws_result,
        )


@dataclass
class Quotation(Resource):
    _endpoint: ClassVar[str] = '/quotation'
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data

    @classmethod
    def create(cls, quotation_request: QuotationRequest) -> 'Quotation':
        response = cls._client.post(
            cls._endpoint, json=quotation_request.to_dict()
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
