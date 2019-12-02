from dataclasses import dataclass


@dataclass
class TrackingRequest:
    tracking_code: str

    def to_dict(self):
        return dict(tracking_code=self.tracking_code,)
