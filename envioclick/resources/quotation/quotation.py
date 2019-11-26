from typing import ClassVar

from envioclick.resources import Resource
from envioclick.resources import QuotationRequest
from envioclick.resources import QuotationResponse


class Quotation(Resource):
    _endpoint: ClassVar[str] = '/quotation'

    @classmethod
    def create(cls, quotation_request: QuotationRequest) -> 'QuotationResponse':
        response = cls._client.post(cls._endpoint, json=quotation_request.to_dict())
        return QuotationResponse(**response)
