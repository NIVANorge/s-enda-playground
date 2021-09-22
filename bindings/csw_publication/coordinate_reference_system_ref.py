from dataclasses import dataclass
from bindings.csw_publication.general_conversion_ref_type import CoordinateReferenceSystemRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CoordinateReferenceSystemRef(CoordinateReferenceSystemRefType):
    class Meta:
        name = "coordinateReferenceSystemRef"
        namespace = "http://www.opengis.net/gml"
