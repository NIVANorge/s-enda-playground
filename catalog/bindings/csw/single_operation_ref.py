from dataclasses import dataclass
from bindings.csw.single_operation_ref_type import SingleOperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class SingleOperationRef(SingleOperationRefType):
    class Meta:
        name = "singleOperationRef"
        namespace = "http://www.opengis.net/gml"
