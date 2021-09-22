from dataclasses import dataclass
from bindings.csw_publication.general_conversion_ref_type import CrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class CrsRef(CrsrefType):
    class Meta:
        name = "crsRef"
        namespace = "http://www.opengis.net/gml"
