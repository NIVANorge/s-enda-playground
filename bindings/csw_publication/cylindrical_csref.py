from dataclasses import dataclass
from bindings.csw_publication.cylindrical_csref_type import CylindricalCsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCsref(CylindricalCsrefType):
    class Meta:
        name = "cylindricalCSRef"
        namespace = "http://www.opengis.net/gml"
