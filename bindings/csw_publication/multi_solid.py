from dataclasses import dataclass
from bindings.csw_publication.multi_solid_type import MultiSolidType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class MultiSolid(MultiSolidType):
    class Meta:
        namespace = "http://www.opengis.net/gml"
