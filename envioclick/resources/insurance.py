from dataclasses import dataclass


@dataclass
class Insurance:
    content_value: float
    amount_insurance: float

    def to_dict(self):
        return dict(
            content_value=self.content_value,
            amount_insurance=self.amount_insurance,
        )
