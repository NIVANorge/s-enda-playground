from dataclasses import dataclass
from bindings.csw_publication.cylindrical_cstype import CylindricalCstype

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CylindricalCs(CylindricalCstype):
    class Meta:
        name = "CylindricalCS"
        namespace = "http://www.opengis.net/gml"
