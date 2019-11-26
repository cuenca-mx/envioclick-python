from typing import ClassVar

from envioclick.resources import Resource
from envioclick.resources.tracking.tracking_request_list import TrackingRequestList
from envioclick.resources.tracking.tracking_response_list import TrackingResponseList


class TrackingBatch(Resource):
    _endpoint: ClassVar[str] = '/track-batch'

    @classmethod
    def retrive_batch(cls, tracking_request: TrackingRequestList) -> 'TrackingResponseList':
        response = cls._client.post(cls._endpoint, json=tracking_request.to_dict())
        return TrackingRequestList(**response)
