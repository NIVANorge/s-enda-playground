from dataclasses import dataclass
from bindings.wfs.execution_status_type import ExecutionStatusType

__NAMESPACE__ = "http://www.opengis.net/wfs/2.0"


@dataclass
class CreateStoredQueryResponseType(ExecutionStatusType):
    pass
