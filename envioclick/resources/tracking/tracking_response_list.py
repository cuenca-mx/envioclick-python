from dataclasses import dataclass
from datetime import datetime
from typing import Dict, List, Union


@dataclass
class DatumClass:
    status: str
    status_detail: str
    arrival_date: datetime
    real_pickup_date: datetime
    real_delivery_date: datetime
    received_by: datetime


@dataclass
class StatusMessage:
    request: str


@dataclass
class TrackingResponseList:
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Dict[str, Union[DatumClass, str]]
