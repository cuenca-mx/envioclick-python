from dataclasses import dataclass
from envioclick.resources.package import Package


@dataclass
class QuotationRequest:
    package: Package
    origin_zip_code: str
    destination_zip_code: str

    def to_dict(self) -> dict:
        return dict(
            originZipCode=self.origin_zip_code,
            destinationZipCode=self.destination_zip_code,
            package=self.package.to_dict(),
        )
