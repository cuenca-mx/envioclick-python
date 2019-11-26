from dataclasses import dataclass
from typing import List


@dataclass
class TrackingRequestList:
    tracking_codes: List[str]

    def to_dict(self):
        return dict(
            tracking_codes=self.tracking_codes
        )
