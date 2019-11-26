from typing import ClassVar


class Resource:
    _client: ClassVar['envio-click.Client']  # type: ignore
    _endpoint: ClassVar[str]
