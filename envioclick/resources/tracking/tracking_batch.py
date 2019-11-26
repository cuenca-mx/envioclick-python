from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, Dict, List, Union

from envioclick.resources import Resource
from envioclick.resources.tracking.tracking_request_list import (
    TrackingRequestList,
)


@dataclass
class DatumClass:
    status: str
    status_detail: str
    arrival_date: datetime
    real_pickup_date: datetime
    real_delivery_date: datetime
    received_by: datetime

    def to_dict(self):
        return dict(
            status=self.status,
            status_detail=self.status_detail,
            arrival_date=self.arrival_date,
            real_pickup_date=self.real_pickup_date,
            real_delivery_date=self.real_delivery_date,
            received_by=self.received_by,
        )


@dataclass
class StatusMessage:
    request: str

    def to_dict(self):
        return dict(
            request=self.request,
        )


class TrackingBatch(Resource):
    _endpoint: ClassVar[str] = '/track-batch'
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Dict[str, Union[DatumClass, str]]

    @classmethod
    def retrive_batc(cls, tracking_request: TrackingRequestList) -> 'TrackingBatch':
        response = cls._client.post(cls._endpoint, json=tracking_request.to_dict())
        return cls(**response)
