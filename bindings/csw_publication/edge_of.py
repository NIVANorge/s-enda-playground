from dataclasses import dataclass
from bindings.csw_publication.composite_curve_type import CurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EdgeOf(CurvePropertyType):
    class Meta:
        name = "edgeOf"
        namespace = "http://www.opengis.net/gml"
