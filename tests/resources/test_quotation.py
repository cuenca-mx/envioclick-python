import pytest

from envioclick import Client
from envioclick.resources import QuotationRequest


@pytest.mark.vcr(record=True)
def test_quotation_request():
    client = Client('wrong_creds')
    d = {
        "package": {
            "description": "Pink iPad",
            "contentValue": 120.01,
            "weight": 1.01,
            "length": 30.01,
            "height": 15.01,
            "width": 20.01,
        },
        "origin_zip_code": "44100",
        "destination_zip_code": "44510",
    }
    qr = QuotationRequest(**d)
    client.quotation.create(qr)
