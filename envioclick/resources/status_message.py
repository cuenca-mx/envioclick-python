from dataclasses import dataclass


@dataclass
class StatusMessage:
    request: str

    def to_dict(self):
        return dict(
            request=self.request
        )
