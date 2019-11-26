from dataclasses import dataclass


@dataclass
class Package:
    description: str
    content_value: float
    weight: float
    length: float
    height: float
    width: float

    def to_dict(self) -> dict:
        return dict(
            description=self.description,
            contentValue=self.content_value,
            weight=self.weight,
            length=self.length,
            height=self.height,
            width=self.width,
        )
