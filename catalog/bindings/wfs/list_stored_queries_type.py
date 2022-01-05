from dataclasses import dataclass
from bindings.wfs.base_request_type import BaseRequestType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class ListStoredQueriesType(BaseRequestType):
    pass
