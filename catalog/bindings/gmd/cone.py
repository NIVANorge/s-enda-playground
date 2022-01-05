from dataclasses import dataclass
from bindings.gmd.cone_type import ConeType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Cone(ConeType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
