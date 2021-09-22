from dataclasses import dataclass
from bindings.csw_publication.operation_method_ref_type import OperationMethodRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class OperationMethodRef(OperationMethodRefType):
    class Meta:
        name = "operationMethodRef"
        namespace = "http://www.opengis.net/gml"
