from dataclasses import dataclass
from bindings.csw.engineering_crsref_type import EngineeringCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class EngineeringCrsref(EngineeringCrsrefType):
    class Meta:
        name = "engineeringCRSRef"
        namespace = "http://www.opengis.net/gml"
