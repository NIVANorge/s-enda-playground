from dataclasses import dataclass
from bindings.csw.operation_ref_type import OperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesOperation(OperationRefType):
    """
    Association to the operation applied to the specified ordinates.
    """
    class Meta:
        name = "usesOperation"
        namespace = "http://www.opengis.net/gml"
