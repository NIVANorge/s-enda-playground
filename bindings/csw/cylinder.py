from dataclasses import dataclass
from bindings.csw.cylinder_type import CylinderType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cylinder(CylinderType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
