from dataclasses import dataclass
from bindings.csw.coordinate_system_ref_type import CoordinateSystemRefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class UsesCs(CoordinateSystemRefType):
    """
    Association to the coordinate system used by this CRS.
    """
    class Meta:
        name = "usesCS"
        namespace = "http://www.opengis.net/gml"
