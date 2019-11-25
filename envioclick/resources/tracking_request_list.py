from dataclasses import dataclass
from typing import List


@dataclass
class TrackingRequestList:
    tracking_codes: List[str]
