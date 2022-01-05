from dataclasses import dataclass
from bindings.csw.operation_parameter_ref_type import OperationParameterRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterRef(OperationParameterRefType):
    class Meta:
        name = "operationParameterRef"
        namespace = "http://www.opengis.net/gml"
