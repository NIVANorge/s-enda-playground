from dataclasses import dataclass
from bindings.csw.pass_through_operation_ref_type import PassThroughOperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class PassThroughOperationRef(PassThroughOperationRefType):
    class Meta:
        name = "passThroughOperationRef"
        namespace = "http://www.opengis.net/gml"
