from dataclasses import dataclass
from bindings.csw.operation_parameter_ref_type import OperationParameterRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationParameterGroupRef(OperationParameterRefType):
    class Meta:
        name = "operationParameterGroupRef"
        namespace = "http://www.opengis.net/gml"
