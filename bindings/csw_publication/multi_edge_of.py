from dataclasses import dataclass
from bindings.csw_publication.multi_curve_property_type import MultiCurvePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiEdgeOf(MultiCurvePropertyType):
    class Meta:
        name = "multiEdgeOf"
        namespace = "http://www.opengis.net/gml"
