from dataclasses import dataclass


@dataclass
class Package:
    description: str
    content_value: float
    weight: float
    length: float
    height: float
    width: float


@dataclass
class QuotationRequest:
    package: Package
    origin_zip_code: str
    destination_zip_code: str
