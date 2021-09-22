from dataclasses import dataclass
from bindings.csw_publication.concatenated_operation_ref_type import ConcatenatedOperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class ConcatenatedOperationRef(ConcatenatedOperationRefType):
    class Meta:
        name = "concatenatedOperationRef"
        namespace = "http://www.opengis.net/gml"
