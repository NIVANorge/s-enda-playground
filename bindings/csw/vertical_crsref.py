from dataclasses import dataclass
from bindings.csw.vertical_crsref_type import VerticalCrsrefType

__NAMESPACE__ = "http://www.opengis.net/gml"


@dataclass
class VerticalCrsref(VerticalCrsrefType):
    class Meta:
        name = "verticalCRSRef"
        namespace = "http://www.opengis.net/gml"
