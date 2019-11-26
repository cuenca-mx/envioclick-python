from dataclasses import dataclass


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

    def to_dict(self):
        return dict(
            id_rates=self.id_rates,
            id_product=self.id_product,
            product=self.product,
            vehicle=self.vehicle,
            id_carrier=self.id_carrier,
            carrier=self.carrier,
            total=self.total,
            delivery_type=self.delivery_type,
            delivery_days=self.delivery_days,
        )
