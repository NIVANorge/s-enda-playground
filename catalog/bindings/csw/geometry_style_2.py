from dataclasses import dataclass
from bindings.csw.geometry_style_property_type import GeometryStylePropertyType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class GeometryStyle2(GeometryStylePropertyType):
    class Meta:
        name = "geometryStyle"
        namespace = "http://www.opengis.net/gml"
