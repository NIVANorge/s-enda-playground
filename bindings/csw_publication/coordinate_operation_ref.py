from dataclasses import dataclass
from bindings.csw_publication.coordinate_operation_ref_type import CoordinateOperationRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateOperationRef(CoordinateOperationRefType):
    class Meta:
        name = "coordinateOperationRef"
        namespace = "http://www.opengis.net/gml"
