from dataclasses import dataclass
from bindings.csw.operation_ref_type import OperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationRef(OperationRefType):
    class Meta:
        name = "operationRef"
        namespace = "http://www.opengis.net/gml"
