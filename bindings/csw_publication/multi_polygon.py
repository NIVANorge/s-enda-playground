from dataclasses import dataclass
from bindings.csw_publication.multi_polygon_type import MultiPolygonType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiPolygon(MultiPolygonType):
    """Deprecated with GML 3.0 and included for backwards compatibility with
    GML 2.

    Use the "MultiSurface" element instead.
    """
    class Meta:
        namespace = "http://www.opengis.net/gml"
