from typing import ClassVar

from envioclick.resources import Resource
from envioclick.resources.tracking.tracking_request import TrackingRequest
from envioclick.resources.tracking.tracking_response import TrackingResponse


class Tracking(Resource):
    _endpoint: ClassVar[str] = '/track'

    @classmethod
    def retrive(cls, tracking_request: TrackingRequest) -> 'TrackingResponse':
        response = cls._client.post(cls._endpoint, json=tracking_request.to_dict())
        return TrackingResponse(**response)
