from dataclasses import dataclass
from bindings.csw.operation_method_ref_type import OperationMethodRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesMethod(OperationMethodRefType):
    """
    Association to the operation method used by this coordinate operation.
    """
    class Meta:
        name = "usesMethod"
        namespace = "http://www.opengis.net/gml"
