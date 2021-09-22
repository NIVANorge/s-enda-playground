from dataclasses import dataclass
from bindings.csw_publication.curve_array_property_type import CurveArrayPropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CurveArrayProperty(CurveArrayPropertyType):
    class Meta:
        name = "curveArrayProperty"
        namespace = "http://www.opengis.net/gml"
