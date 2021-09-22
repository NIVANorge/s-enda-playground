from dataclasses import dataclass
from bindings.csw_publication.solid_type import SolidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class Solid1(SolidType):
    class Meta:
        name = "Solid"
        namespace = "http://www.opengis.net/gml"
