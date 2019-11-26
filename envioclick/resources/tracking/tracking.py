from dataclasses import dataclass
from datetime import datetime
from typing import ClassVar, List

from envioclick.resources import Resource
from envioclick.resources.status_message import StatusMessage
from envioclick.resources.tracking.tracking_request import TrackingRequest


@dataclass
class Data:
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


class Tracking(Resource):
    _endpoint: ClassVar[str] = '/track'
    status: str
    status_codes: List[int]
    status_messages: List[StatusMessage]
    data: Data

    @classmethod
    def retrive(cls, tracking_request: TrackingRequest) -> 'Tracking':
        response = cls._client.post(cls._endpoint, json=tracking_request.to_dict())
        return cls(**response)

    def to_dict(self):
        return dict(
            status=self.status,
            status_codes=self.status_codes,
            status_messages=[message.to_dict() for message in self.status_messages],
            data=self.data.to_dict()
        )
