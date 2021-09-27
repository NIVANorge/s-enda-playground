from dataclasses import dataclass
from bindings.gmd.dmsangle_type import DmsangleType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class DmsAngle(DmsangleType):
    class Meta:
        name = "dmsAngle"
        namespace = "http://www.opengis.net/gml"
